# Generated by Django 4.2.9 on 2024-01-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_remove_property_plan_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='contract_document',
        ),
    ]
