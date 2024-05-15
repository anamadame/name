from django_filters.rest_framework import FilterSet
from .models import *

class FoodFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'price': ['gt', 'lt']

        }