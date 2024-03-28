from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required
from .models import Customer, Profile, Property, Sales, Payment, UserProfile, PaymentPlan, ConstructionPhase, PropertyStatus
from .forms import CustomerForm, PropertyForm, SalesForm, PaymentForm, ConstructionPhaseForm, PaymentPlanForm
from .forms import UserSignUpForm, LoginForm, UserCreationForm, ProfileForm
from django.contrib import messages
from datetime import date, timedelta
from .models import Customer, Property, Sales, Payment, UserProfile
from .forms import CustomerForm, PropertyForm, SalesForm, PaymentForm, PropertyStatusForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
from django_filters.views import FilterView
from .filters import PropertyFilter



def user_has_role(user, roles):
    return user.is_authenticated and (user.userprofile.role in roles or user.userprofile.role == 'Manager')

def property_status(request):
    filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'sales/property_status.html', {'filter': filter})

def update_property_status(request, pk):
    property_status = get_object_or_404(PropertyStatus, property__pk=pk)
    
    if request.method == 'POST':
        form = PropertyStatusForm(request.POST, instance=property_status)
        if form.is_valid():
            form.save()
            return redirect('property_status')  # Redirect to the property list view
    else:
        form = PropertyStatusForm(instance=property_status)
    
    return render(request, 'sales/property_status_form.html', {'form': form})

@login_required
def update_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # This ensures a profile exists
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_update.html', {'profile_form': profile_form})

#def stock_dashboard(request):
#    available_properties = Property.objects.filter(property_status__status='Available')
#    filter = PropertyFilter(request.GET, queryset=available_properties)
 #   return render(request, 'sales/stock_dashboard.html', {'filter': filter})

def stock_dashboard(request):
    filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'sales/stock_dashboard.html', {'filter': filter})


def index(request):
    return render (request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered!")
            return redirect('my-login')  # Redirect to the dashboard or any other page
    else:
        form = UserSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully Logged in!")
                return redirect('dashboard')  # Redirect to a default page for all users
    context = {'form': form}
    return render(request, 'registration/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("index")




@login_required(login_url='my-login')
def add_payment(request, pk):
    if not user_has_role(request.user, ['Finance', 'Collections', 'Manager']):
        return  render(request, '403.html') 
    sale = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.sales = sale
            payment.payment_number = Payment.objects.filter(sales=sale).count() + 1
            payment.payment_date = date.today()
            payment.due_date = payment.payment_date + timedelta(days=115)  # Example: 30 days after payment_date
            payment.is_paid = True  # Assuming payment is made as soon as it's recorded
            payment.save()
            return redirect('payment_list')  # Redirect to the sales list or appropriate page
    else:
        form = PaymentForm()
    return render(request, 'sales/add_payment.html', {'form': form, 'sale': sale})



@login_required(login_url='my-login')
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {}
    if user_profile.role == 'Marketing':
        context['customers'] = Customer.objects.all()
        context['sales'] = Sales.objects.all()
        return render(request, 'sales/marketing_dashboard.html', context)
    elif user_profile.role == 'Design':
        context['properties'] = Property.objects.all()
        return render(request, 'sales/design_dashboard.html', context)
    elif user_profile.role == 'Finance':
        context['payments'] = Payment.objects.all()
        return render(request, 'sales/finance_dashboard.html', context)
    elif user_profile.role == 'Collection':
        due_payments = Payment.objects.filter(due_date__lte=date.today())
        return render(request, 'sales/collection_dashboard.html', {'due_payments': due_payments})
    elif user_profile.role == 'Manager':
        total_properties = Property.objects.count()
        sold_properties = Sales.objects.count()
        available_properties = total_properties - sold_properties

        context = {
            'total_properties': total_properties,
            'sold_properties': sold_properties,
            'available_properties': available_properties,
        }
        
        # Add logic for manager dashboard
        return render(request, 'sales/manager_dashboard.html', context)
    else:
        return render(request, '403.html')
    


def send_payment_reminders():
    overdue_payments = Payment.objects.filter(due_date__lte=date.today(), is_paid=False)
    for payment in overdue_payments:
        context = {
            'customer_name': payment.sales.customer.name,
            'property_details': payment.sales.property.location,
            'due_date': payment.due_date,
        }
        subject = 'Payment Reminder'
        html_message = render_to_string('emails/payment_reminder_email.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'from@example.com'
        to = payment.sales.customer.email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)

@login_required(login_url='my-login')
def customer_list(request):
    if not user_has_role(request.user, ['Marketing', 'Manager']):
        return render(request, '403.html')
    customers = Customer.objects.all()
    return render(request, 'sales/customer_list.html', {'customers': customers})

@login_required(login_url='my-login')
def customer_detail(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager']):
        return render(request, '403.html')
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'sales/customer_detail.html', {'customer': customer})

@login_required(login_url='my-login')
def customer_create(request):
    if not user_has_role(request.user, ['Marketing', 'Manager']):
        return render(request, '403.html')
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'sales/customer_form.html', {'form': form})

@login_required(login_url='my-login')
def customer_update(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager']):
        return render(request, '403.html')
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'sales/customer_form.html', {'form': form})

@login_required(login_url='my-login')
def customer_delete(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager']):
        return render(request, '403.html')
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'sales/customer_confirm_delete.html', {'customer': customer})

@login_required(login_url='my-login')
def property_list(request):
    if not user_has_role(request.user, ['Design', 'Manager']):
        return render(request, '403.html')
    properties = Property.objects.all()
    return render(request, 'sales/property_list.html', {'properties': properties})

@login_required(login_url='my-login')
def property_detail(request, pk):
    if not user_has_role(request.user, ['Design', 'Manager']):
        return render(request, '403.html')
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'sales/property_detail.html', {'property': property})

@login_required(login_url='my-login')
def property_create(request):
    if not user_has_role(request.user, ['Design', 'Manager']):
        return render(request, '403.html')
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'sales/property_form.html', {'form': form})

@login_required(login_url='my-login')
def property_update(request, pk):
    if not user_has_role(request.user, ['Design', 'Manager']):
        return render(request, '403.html')
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'sales/property_form.html', {'form': form})

@login_required(login_url='my-login')
def property_delete(request, pk):
    if not user_has_role(request.user, ['Design', 'Manager']):
        return render(request, '403.html')
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'sales/property_confirm_delete.html', {'property': property})

# Construction Phase Views
@login_required(login_url='my-login')
def construction_phase_list(request):
    phases = ConstructionPhase.objects.all()
    return render(request, 'sales/construction_phase_list.html', {'phases': phases})

@login_required(login_url='my-login')
def construction_phase_detail(request, pk):
    phase = get_object_or_404(ConstructionPhase, pk=pk)
    return render(request, 'sales/construction_phase_detail.html', {'phase': phase})

@login_required(login_url='my-login')
def construction_phase_create(request):
    if request.method == 'POST':
        form = ConstructionPhaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('construction_phase_list')
    else:
        form = ConstructionPhaseForm()
    return render(request, 'sales/construction_phase_form.html', {'form': form})

@login_required(login_url='my-login')
def construction_phase_update(request, pk):
    phase = get_object_or_404(ConstructionPhase, pk=pk)
    if request.method == 'POST':
        form = ConstructionPhaseForm(request.POST, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('construction_phase_detail', pk=phase.pk)
    else:
        form = ConstructionPhaseForm(instance=phase)
    return render(request, 'sales/construction_phase_form.html', {'form': form})

@login_required(login_url='my-login')
def construction_phase_delete(request, pk):
    phase = get_object_or_404(ConstructionPhase, pk=pk)
    if request.method == 'POST':
        phase.delete()
        return redirect('construction_phase_list')
    return render(request, 'sales/construction_phase_confirm_delete.html', {'phase': phase})

@login_required(login_url='my-login')
def sales_list(request):
    if not user_has_role(request.user, ['Marketing', 'Manager', 'Collection']):
        return render(request, '403.html')
    sales = Sales.objects.all()
    return render(request, 'sales/sales_list.html', {'sales': sales})

@login_required(login_url='my-login')
def sale_detail(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager', 'Collection']):
        return render(request, '403.html')
    sale = get_object_or_404(Sales, pk=pk)
    return render(request, 'sales/sale_detail.html', {'sale': sale})

@login_required(login_url='my-login')
def sale_create(request):
    if not user_has_role(request.user, ['Marketing', 'Manager', 'Collection']):
        return render(request, '403.html')
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesForm()
    return render(request, 'sales/sale_form.html', {'form': form})

@login_required(login_url='my-login')
def sale_update(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager', 'Collection']):
        return render(request, '403.html')
    sale = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_detail', pk=sale.pk)
    else:
        form = SalesForm(instance=sale)
    return render(request, 'sales/sale_form.html', {'form': form})

@login_required(login_url='my-login')
def sale_delete(request, pk):
    if not user_has_role(request.user, ['Marketing', 'Manager', 'Collection']):
        return render(request, '403.html')
    sale = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sales_list')
    return render(request, 'sales/sale_confirm_delete.html', {'sale': sale})

# Payment Views

@login_required(login_url='my-login')
def payment_list(request):
    if not user_has_role(request.user, ['Finance', 'Collections', 'Manager']):
        return render(request, '403.html')
    payments = Payment.objects.all()
    return render(request, 'sales/payment_list.html', {'payments': payments})

@login_required(login_url='my-login')
def payment_detail(request, pk):
    if not user_has_role(request.user, ['Finance', 'Collections', 'Manager']):
        return render(request, '403.html')
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'sales/payment_detail.html', {'payment': payment})

