from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# from .views import employee_assets_api
# from django.contrib.auth import views as auth_views 
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('asset_list/', views.asset_list, name='asset_list'),
    path('employee_list/', views.employee_asset_list, name='employee_asset_list'),
    path('upload_employees/', views.employee_upload, name='employee_upload'),
    path('upload_success/', views.employee_upload_success, name='employee_upload_success'),
    path('asset_dashboard/', views.asset_dashboard, name='asset_dashboard'),
    # path('api/<employee_id>/', employee_assets_api, name='employee_assets_api'),
    path('', include(router.urls)),
]
