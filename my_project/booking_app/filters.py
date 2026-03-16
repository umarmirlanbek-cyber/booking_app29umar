from django_filters.rest_framework import FilterSet, BaseInFilter
from .models import Hotel,Room

class HotelFilter(FilterSet):
    service = BaseInFilter(field_name='service__id', lookup_expr='in')
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city':['exact'],
            'hotel_stars':['exact'],
        }

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status':['exact'],
            'price':['gt','lt']
        }