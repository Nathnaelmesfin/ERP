# Generated by Django 5.0.1 on 2024-01-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_employee_department_employee_habesha_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_id_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
