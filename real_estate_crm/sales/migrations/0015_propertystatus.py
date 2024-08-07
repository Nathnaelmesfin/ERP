# Generated by Django 4.2.9 on 2024-03-19 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_alter_payment_agreement_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Held', 'Held'), ('Reserved', 'Reserved'), ('BTS Coming', 'BTS Coming'), ('BTS/MOU Received', 'BTS/MOU Received'), ('Sold', 'Sold')], default='Available', max_length=20)),
                ('reserved_until', models.DateTimeField(blank=True, help_text='The deadline for initial payment for reserved properties', null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='property_status', to='sales.property')),
            ],
        ),
    ]
