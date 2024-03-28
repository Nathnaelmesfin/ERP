from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index1'),
    path('search/', views.SearchResultsView.as_view(), name='search_result'),
    path('inventorys/', views.InventoryListView.as_view(), name='inventory'),
    path('devices/', views.DeviceListView.as_view(), name='devices'),
    path('device/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('trackers/', views.TrackerListView.as_view(), name='trackers'),
    path('tracker/<int:pk>/', views.TrackerDetailView.as_view(), name='tracker_detail'),
]