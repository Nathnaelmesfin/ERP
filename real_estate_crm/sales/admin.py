from django.contrib import admin
from .models import (UserProfile, Customer, UnitType, BalconyType, PropertyLootNumber, PropertyBlock, Property, Sales, PaymentPlan, ConstructionPhase, Payment, PropertyStatus)
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Optionally, you can customize how models are displayed in the admin

class PropertyStatusAdmin(admin.ModelAdmin):
    list_display = ('property', 'status', 'reserved_until')
    search_fields = ('property', 'status')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')
    search_fields = ('name',)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('house_no', 'location', 'site', 'block', 'loot_number', 'net_area', 'status_display')
    search_fields = ('house_no', 'location', 'site', 'block', 'loot_number', 'net_area', 'status_display')
    
    def status_display(self, obj):
        return obj.property_status.status
    status_display.short_description = 'Status'

class SalesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'property', 'contract_amount', 'contract_date')
    list_filter = ('contract_date',)
    search_fields = ('customer__name', 'property__location')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('sales', 'payment_number', 'amount', 'payment_date', 'is_paid')
    list_filter = ('payment_date', 'is_paid')
    search_fields = ('sales__customer__name', 'sales__property__location')

class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('user', 'role')
    search_fields = ('user', 'role')

# Resource classes
class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer

class UnitTypeResource(resources.ModelResource):
    class Meta:
        model = UnitType

class BalconyTypeResource(resources.ModelResource):
    class Meta:
        model = BalconyType

class PropertyLootNumberResource(resources.ModelResource):
    class Meta:
        model = PropertyLootNumber

class PropertyBlockResource(resources.ModelResource):
    class Meta:
        model = PropertyBlock

class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property

class SalesResource(resources.ModelResource):
    class Meta:
        model = Sales

class PaymentPlanResource(resources.ModelResource):
    class Meta:
        model = PaymentPlan

class ConstructionPhaseResource(resources.ModelResource):
    class Meta:
        model = ConstructionPhase

class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment

# Admin classes
class UserProfileAdmin(ImportExportModelAdmin):
    resource_class = UserProfileResource

class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

class UnitTypeAdmin(ImportExportModelAdmin):
    resource_class = UnitTypeResource

class BalconyTypeAdmin(ImportExportModelAdmin):
    resource_class = BalconyTypeResource

class PropertyLootNumberAdmin(ImportExportModelAdmin):
    resource_class = PropertyLootNumberResource

class PropertyBlockAdmin(ImportExportModelAdmin):
    resource_class = PropertyBlockResource

class PropertyAdmin(ImportExportModelAdmin):
    resource_class = PropertyResource

class SalesAdmin(ImportExportModelAdmin):
    resource_class = SalesResource

class PaymentPlanAdmin(ImportExportModelAdmin):
    resource_class = PaymentPlanResource

class ConstructionPhaseAdmin(ImportExportModelAdmin):
    resource_class = ConstructionPhaseResource

class PaymentAdmin(ImportExportModelAdmin):
    resource_class = PaymentResource

# Register your models here
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(UnitType, UnitTypeAdmin)
admin.site.register(BalconyType, BalconyTypeAdmin)
admin.site.register(PropertyLootNumber, PropertyLootNumberAdmin)
admin.site.register(PropertyBlock, PropertyBlockAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(PaymentPlan, PaymentPlanAdmin)
admin.site.register(ConstructionPhase, ConstructionPhaseAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PropertyStatus, PropertyStatusAdmin)