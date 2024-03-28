from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Max
from django.utils import timezone
from django.http import request
from django.db.models.signals import post_save
from django.dispatch import receiver
from ethiopian_date import EthiopianDateConverter

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

# Signal to create or update the user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Design', 'Design'),
        ('Finance', 'Finance'),
        ('Collection', 'Collection'),
        ('Manager', 'Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UnitType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class BalconyType(models.Model):
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description

class PropertyLootNumber(models.Model):
    loot_number = models.CharField(max_length=100)
    
    def __str__(self):
        return self.loot_number


class PropertyBlock(models.Model):
    block = models.CharField(max_length=100)
    
    def __str__(self):
        return self.block

class Property(models.Model):
    house_no = models.CharField(max_length=50, unique=True, null=True)
    location = models.CharField(max_length=200)
    subcity = models.CharField(max_length=50, null=True, blank=True)
    woreda = models.CharField(max_length=50, null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)
    loot_number = models.ForeignKey(PropertyLootNumber, on_delete=models.CASCADE, null=True)
    block = models.ForeignKey(PropertyBlock, on_delete=models.CASCADE, null=True)
    floor = models.IntegerField(null=True, blank=True)
    bedroom_number = models.IntegerField(null=True, blank=True)
    kitchen = models.IntegerField(null=True, blank=True)
    living_room = models.IntegerField(null=True, blank=True)
    toilet = models.IntegerField(null=True, blank=True)
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE, null=True)
    balcony_type = models.ForeignKey(BalconyType, on_delete=models.CASCADE, null=True)
    extra_balconies = models.IntegerField(null=True, blank=True)
    balcony_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gross_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    common_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_units_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_floor_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    has_lift = models.BooleanField(default=False, null=True, blank=True)
    has_generator = models.BooleanField(default=False, null=True, blank=True)
    has_parking = models.BooleanField(default=False, null=True, blank=True)
    has_water_pump = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    marketing_director = models.CharField(max_length=100, null=True, blank=True)
    supervisor_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return f"{self.house_no} - {self.site}"

class PropertyStatus(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Held', 'Held'),
        ('Reserved', 'Reserved'),
        ('BTS Coming', 'BTS Coming'),
        ('BTS/MOU Received', 'BTS/MOU Received'),
        ('Sold', 'Sold'),
    ]
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='property_status')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    reserved_until = models.DateTimeField(null=True, blank=True, help_text='The deadline for initial payment for reserved properties')

    def __str__(self):
        return f"{self.property.house_no} - {self.status}"

        
class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agreement_number = models.CharField(max_length=100, null=True)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_amount_birr = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit_price_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_plan = models.ForeignKey('PaymentPlan', on_delete=models.CASCADE, null=True)       
    contract_date = models.DateField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True)    
    branch = models.CharField(max_length=100, null=True)
    sold_via = models.CharField(max_length=100, null=True)
    total_paid_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    property_type = models.CharField(max_length=50, null=True)
    finish_type = models.CharField(max_length=50, null=True)
    delivery_date_in_months = models.IntegerField(null=True)
    sales_supervisor = models.CharField(max_length=100, null=True)
    sales_consultant = models.CharField(max_length=100, null=True)
    remark = models.TextField(blank=True, null=True)
    #contract_document = models.FileField(upload_to='contract_documents/', null=True)
    def ethiopian_contract_date(self):
        # Ethiopian months mapping
        ethiopian_months = {
            1: 'መስከረም ',
            2: 'ጥቅምት',
            3: 'ህዳር',
            4: 'ታኅሣሥ',
            5: 'ጥር',
            6: 'የካቲት',
            7: 'መጋቢት',
            8: 'ሚያዝያ',
            9: 'ግንቦት',
            10: 'ሰኔ',
            11: 'ሐምሌ',
            12: 'ነሐሴ',
            13: 'ጳጉሜ',
        }

        if self.contract_date:
            # Correctly handling the tuple returned by the conversion function
            eth_year, eth_month, eth_day = EthiopianDateConverter.to_ethiopian(self.contract_date.year, self.contract_date.month, self.contract_date.day)
            month_name = ethiopian_months.get(eth_month, "Unknown")
            formatted_date = f"{month_name[:3]}. {eth_day}, {eth_year}"  # Using abbreviation for month
            return formatted_date
        return None
    def __str__(self):
        return f"{self.customer.name} - {self.property.house_no}"

class PaymentPlan(models.Model):
    description = models.CharField(max_length=200, help_text="A short description of the payment plan", null=True)
    down_payment_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage of the total price required as down payment", null=True)
    number_of_installments = models.IntegerField(help_text="Total number of monthly installments", null=True)
    monthly_payment_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage of the remaining amount to be paid monthly after down payment", null=True)

    def __str__(self):
        return self.description



class ConstructionPhase(models.Model):
    phase_description = models.CharField(max_length=200)
    # Add more fields as needed

    def __str__(self):
        return self.phase_description

class Payment(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    agreement_number = models.CharField(max_length=100, null=True, blank=True, help_text="* The agreement number for this payment")
    payment_number = models.IntegerField()
    installment_number = models.IntegerField(null=True, blank=True, help_text="The installment number for this payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=6, decimal_places=2)
    percentage_paid = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    invoice_number = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    prepared_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_date = models.DateField()
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    remark = models.TextField(blank=True, null=True)
    payment_recipt = models.FileField(upload_to='payment_recipts/', null=True)
    is_overdue = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:  # On first save
            if self.installment_number is None:
                # Set installment_number based on the number of existing payments for the same sale
                self.installment_number = Payment.objects.filter(sales=self.sales).count() + 1
            # Calculate due_date based on installment_number and PaymentPlan
            # This is simplified; you'll need to adjust it based on your payment plan logic
            if self.installment_number == 1:
                self.due_date = self.sales.contract_date + relativedelta(months=1)  # Assuming the first payment is due one month after contract
            else:
                self.due_date = self.sales.contract_date + relativedelta(months=self.installment_number)
            if not self.prepared_by:
                self.prepared_by = request.user.username
        super(Payment, self).save(*args, **kwargs)
    
    def update_overdue_payments():
        today = timezone.now().date()  # Get today's date in the project's time zone
        overdue_payments = Payment.objects.filter(due_date__lte=today, is_paid=False)
        overdue_payments.update(is_overdue=True)
    #def save(self, *args, **kwargs):
        # Logic for setting due_date
       # if not self.id:  # Runs only when the payment is first created
         #   if self.payment_number == 1:
                # For the first payment, due date is 4 months from the contract date
           #     self.due_date = self.sales.contract_date + relativedelta(months=4)
           # else:
                # For subsequent payments, find the last payment date
             #   last_payment = Payment.objects.filter(
             #       sales=self.sales,
              #      payment_number=self.payment_number - 1
            #    ).order_by('-payment_date').first()

             #   if last_payment:
                    # Set due date to 4 months after the last payment's payment date
            #        self.due_date = last_payment.payment_date + relativedelta(months=4)
             #   else:
                    # Fallback logic for any unexpected scenarioS
             #       self.due_date = date.today() + relativedelta(months=4)

     #   super(Payment, self).save(*args, **kwargs)
    



    @property
    def is_overdue(self):
        if self.is_paid:
            return self.payment_date > self.due_date
        else:
            return date.today() > self.due_date

    @property
    def remaining_amount(self):
        total_paid = Payment.objects.filter(sales=self.sales).aggregate(models.Sum('amount'))['amount__sum'] or 0
        return self.sales.contract_amount - total_paid

    def __str__(self):
        return f"{self.sales} - Payment {self.payment_number}"
