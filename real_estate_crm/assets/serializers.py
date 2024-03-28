# serializers.py in your app directory

from rest_framework import serializers
from .models import Employee, Asset

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id_no', 'department', 'position', 'name', 'habesha_name', 'subcity', 'woreda', 'house_num', 'phone_number', 'sim_type', 'photo_number', 'last_id_no']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['item_type', 'item_model', 'taken_date', 'employee']
