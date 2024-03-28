from django import forms
from .models import Profile, Customer, Property, Sales, Payment,  PaymentPlan, ConstructionPhase, PropertyStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import *


class PropertyStatusForm(forms.ModelForm):
    class Meta:
        model = PropertyStatus
        fields = ('status', 'property', 'reserved_until')
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'reserved_until': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding an email field, for instance

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'profile_picture')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['sales', 'agreement_number','payment_number', 'amount', 'exchange_rate', 'percentage_paid','invoice_number', 'bank', 'payment_date']
        # Add or remove fields based on your Payment model
        widgets = {
            'sales': forms.Select(attrs={'class': 'form-control'}),
            'agreement_number': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_number': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'exchange_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'percentage_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'gender', 'address', 'phone_number', 'email', 'contact_info']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        } 
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'  # Include all fields from the Property model
        widgets = {
            'loot_number': forms.Select(attrs={'class': 'form-control'}),
            'block:': forms.Select(attrs={'class': 'form-control'}),
            'unit_type': forms.Select(attrs={'class': 'form-control'}),
            'balcony_type': forms.Select(attrs={'class': 'form-control'}),

            'site': forms.TextInput(attrs={'class': 'form-control'}),  
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'subcity': forms.TextInput(attrs={'class': 'form-control'}),
            'woreda': forms.TextInput(attrs={'class': 'form-control'}),
            'block': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'position_floor': forms.TextInput(attrs={'class': 'form-control'}),
            'view': forms.TextInput(attrs={'class': 'form-control'}),
            'bedroom_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'kitchen': forms.NumberInput(attrs={'class': 'form-control'}),
            'living_room': forms.NumberInput(attrs={'class': 'form-control'}),
            'toilet': forms.NumberInput(attrs={'class': 'form-control'}),
            'apartment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'extra_balconies': forms.NumberInput(attrs={'class': 'form-control'}),
            'balcony_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'net_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'gross_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'common_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_units_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_floor_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_lift': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_generator': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_parking': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_water_pump': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'project_type': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'marketing_director': forms.TextInput(attrs={'class': 'form-control'}),
            'supervisor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            #'plan_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }
class PropertyFilterForm(forms.Form):
    class Meta:
        model = Property
        fields = ['location', 'site', 'loot_number', 'block', 'floor', 'bedroom_number', 'unit_type', 'balcony_type', 'extra_balconies', 'has_lift', 'has_generator', 'has_parking', 'has_water_pump', 'net_area', 'gross_area', 'common_area', 'total_units_area', 'total_floor_area', 'price', 'status__status']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'loot_number': forms.Select(attrs={'class': 'form-control'}),
            'block': forms.Select(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedroom_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_type': forms.Select(attrs={'class': 'form-control'}),
            'balcony_type': forms.Select(attrs={'class': 'form-control'}),
            'extra_balconies': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_lift': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_generator': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_parking': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'has_water_pump': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'net_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'gross_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'common_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_units_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_floor_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class PaymentPlanForm(forms.ModelForm):
    class Meta:
        model = PaymentPlan
        fields = ['description']
        # Add any other fields that you have in your PaymentPlan model

class ConstructionPhaseForm(forms.ModelForm):
    class Meta:
        model = ConstructionPhase
        fields = ['phase_description']
        # Add any other fields that you have in your ConstructionPhase model

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'  # Include all fields of the Sales model
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'property': forms.Select(attrs={'class': 'form-control'}),
            'agreement_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'contract_amount_birr': forms.NumberInput(attrs={'class': 'form-control'}),
            'exchange_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price_usd': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_plan': forms.Select(attrs={'class': 'form-control'}),
            'contract_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'sold_via': forms.TextInput(attrs={'class': 'form-control'}),
            'total_paid_percent': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control'}),
            'finish_type': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_date_in_months': forms.NumberInput(attrs={'class': 'form-control'}),
            'sales_supervisor': forms.TextInput(attrs={'class': 'form-control'}),
            'sales_consultant': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
            #'contract_document': forms.FileInput(attrs={'class': 'form-control'}),
            # ... Add widgets for other fields as needed
        }
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
            'class': 'form-control',  # Add custom CSS class
            'placeholder': 'User Name',  # Add placeholder text
            'autocomplete': 'off',  # Disable autocomplete
        }))
    password = forms.CharField(widget=PasswordInput(attrs={
            'class': 'form-control',  # Add custom CSS class
            'placeholder': 'Your password',  # Add placeholder text
            'autocomplete': 'off',  # Disable autocomplete
        }))

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user