from django.shortcuts import render
from .models import Employee,Asset
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models.functions import TruncDay
from django.db.models import Prefetch
from django.http import JsonResponse
# from .decorators import api_key_required
from rest_framework import viewsets
from .serializers import EmployeeSerializer




# def asset_list(request):
#     assets = Asset.objects.all()
#     return render(request, 'assets/asset_list.html', {'assets': assets})
def asset_list(request):
    employees = Employee.objects.prefetch_related(
        Prefetch('asset_set', queryset=Asset.objects.order_by('taken_date'))
    )
    return render(request, 'assets/asset_list.html', {'employees': employees})

def employee_asset_list(request):
    employees = Employee.objects.prefetch_related('asset_set').all()
    return render(request, 'assets/employee_asset_list.html', {'employees': employees})

def import_employees_from_csv(file):
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        Employee.objects.create(
            # ... [fields as in the function you created]
            id_no=row['ID no'],
            department=row['Department'],
            position=row['position'],
            name=row['Name'],
            habesha_name=row['ስም'],
            subcity=row['subcity'],
            woreda=row['WOREDA'],
            house_num=row['HOUSE NO'],
            phone_number=row['Tel no'],
            sim_type=row['Sim Type'],
            photo_number=row['photo no'],
            last_id_no=row['last ID no']
        )

def employee_upload(request):
    if request.method == "POST":
        csv_file = request.FILES['file']
        import_employees_from_csv(csv_file)
        return redirect('employee_upload_success')  # Redirect to a success page or similar
    return render(request, 'assets/employee_upload.html')

# Add a success view or handle it as you see fit
def employee_upload_success(request):
    return HttpResponse("Employees imported successfully.")
@login_required
def asset_dashboard(request):
    # Get counts for all required statistics
    total_assets_count = Asset.objects.count()
    total_employees_count = Employee.objects.count()
    today = timezone.now().date()
    assets_registered_today_count = Asset.objects.filter(taken_date=today).count()

    # Create context to pass to the template
    context = {
        'total_assets_count': total_assets_count,
        'total_employees_count': total_employees_count,
        'assets_registered_today_count': assets_registered_today_count,
    }

    return render(request, 'assets/dashboard.html', context)
# @api_key_required
# def employee_assets_api(request, employee_id):
#     # Find the employee by ID
#     try:
#         employee = Employee.objects.get(id_no=employee_id)
#         # Fetch related assets
#         assets = employee.asset_set.all()
#     except Employee.DoesNotExist:
#         return JsonResponse({'error': 'Employee not found'}, status=404)
    
#     # Construct the list of assets
#     assets_list = [
#         {
#             'item_type': asset.item_type,
#             'item_model': asset.item_model,
#             'taken_date': asset.taken_date
#         } for asset in assets
#     ]
    
#     # Construct employee detail info
#     employee_info = {
#         'id_no': employee.id_no,
#         'department': employee.department,
#         'position': employee.position,
#         'name': employee.name,
#         'habesha_name': employee.habesha_name,
#         'subcity': employee.subcity,
#         'woreda': employee.woreda,
#         'house_num': employee.house_num,
#         'phone_number': employee.phone_number,
#         'sim_type': employee.sim_type,
#         'photo_number': employee.photo_number,
#         'last_id_no': employee.last_id_no,
#     }
    
#     # Return the response in JSON format
#     return JsonResponse({
#         'employee': employee_info,
#         'assets': assets_list
#     })
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer