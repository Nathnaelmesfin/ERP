import django_filters
from .forms import PropertyFilterForm
from .models import Property, PropertyStatus

class PropertyFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = django_filters.NumberFilter(field_name="net_area", lookup_expr='gte')
    max_area = django_filters.NumberFilter(field_name="net_area", lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['location', 'site', 'loot_number', 'block', 'floor', 'bedroom_number', 'unit_type', 'balcony_type', 'extra_balconies', 'has_lift', 'has_generator', 'has_parking', 'has_water_pump', 'net_area', 'gross_area', 'common_area', 'total_units_area', 'total_floor_area', 'price', 'status__status']
        form = PropertyFilterForm