from django.urls import path
from . import views
from .views import signup
from .views import stock_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index' ),
    path('dashboard/', views.dashboard, name='dashboard'),

    # User profile URLs
    path('profile/update/', views.update_profile, name='update_profile'),
    
    # Sales URLs
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/add_payment/<int:pk>/', views.add_payment, name='add_payment'),
    path('sales/payment_detail/<int:pk>/', views.payment_detail, name='payment_detail'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/new/', views.customer_create, name='customer_create'),
    path('customer/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # Property URLs
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/new/', views.property_create, name='property_create'),
    path('property/<int:pk>/edit/', views.property_update, name='property_update'),
    path('property/<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('property/status/', views.property_status, name='property_status'),
    path('property/<int:pk>/status/', views.update_property_status, name='update_property_status'),
    # Payment URLs
    path('payments/', views.payment_list, name='payment_list'),
    path('payment/<int:pk>/', views.payment_detail, name='payment_detail'),
   
    # Construction Phase URLs
    path('construction_phases/', views.construction_phase_list, name='construction_phase_list'),
    path('construction_phase/<int:pk>/', views.construction_phase_detail, name='construction_phase_detail'),
    path('construction_phase/new/', views.construction_phase_create, name='construction_phase_create'),
    path('construction_phase/<int:pk>/edit/', views.construction_phase_update, name='construction_phase_update'),
    path('construction_phase/<int:pk>/delete/', views.construction_phase_delete, name='construction_phase_delete'),

    # Sales URLs
    path('sales/', views.sales_list, name='sale_list'),
    path('sale/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sale/new/', views.sale_create, name='sale_create'),
    path('sale/<int:pk>/edit/', views.sale_update, name='sale_update'),
    path('sale/<int:pk>/delete/', views.sale_delete, name='sale_delete'),

     # Additional URLs as needed
    path('signup/', signup, name='signup'),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('stock-dashboard/', stock_dashboard, name='stock-dashboard'),
    

]
