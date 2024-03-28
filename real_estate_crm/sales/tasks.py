from celery import shared_task
from django.core.mail import send_mail
from .models import Payment
from datetime import datetime

@shared_task
def send_overdue_payment_notifications():
    overdue_payments = Payment.objects.filter(due_date__lt=datetime.now(), is_paid=False)
    for payment in overdue_payments:
        send_mail(
            'Overdue Payment Notification',
            f'Your payment for {payment.sales} is overdue.',
            'your-email@example.com',
            [payment.sales.customer.contact_info],
            fail_silently=False,
        )

@shared_task
def update_overdue_payments_celery():
    update_overdue_payments() 