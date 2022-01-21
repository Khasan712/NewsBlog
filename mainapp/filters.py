import django_filters
from .models import *

class NewsPostFilter(django_filters.FilterSet):
    class Meta:
        model = NewsPost
        fields = {
            'description':['icontains'],
            # 'message':['icontains'],
            # 'title':['icontains'],
        }