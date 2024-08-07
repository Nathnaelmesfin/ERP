# Generated by Django 5.0.1 on 2024-01-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='habesha_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='house_num',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='sim_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='subcity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='woreda',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
