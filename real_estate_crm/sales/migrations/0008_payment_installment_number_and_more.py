# Generated by Django 4.2.9 on 2024-02-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='installment_number',
            field=models.IntegerField(blank=True, help_text='The installment number for this payment', null=True),
        ),
        migrations.AddField(
            model_name='paymentplan',
            name='down_payment_percentage',
            field=models.DecimalField(decimal_places=2, help_text='Percentage of the total price required as down payment', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='paymentplan',
            name='monthly_payment_percentage',
            field=models.DecimalField(decimal_places=2, help_text='Percentage of the remaining amount to be paid monthly after down payment', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='paymentplan',
            name='number_of_installments',
            field=models.IntegerField(help_text='Total number of monthly installments', null=True),
        ),
        migrations.AlterField(
            model_name='paymentplan',
            name='description',
            field=models.CharField(help_text='A short description of the payment plan', max_length=200, null=True),
        ),
    ]