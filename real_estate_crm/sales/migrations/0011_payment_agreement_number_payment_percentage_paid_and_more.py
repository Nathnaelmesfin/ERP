# Generated by Django 4.2.9 on 2024-03-15 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0010_remove_property_apartment_type_remove_property_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='agreement_number',
            field=models.CharField(blank=True, help_text='The agreement number for this payment', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='percentage_paid',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='prepared_by',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
