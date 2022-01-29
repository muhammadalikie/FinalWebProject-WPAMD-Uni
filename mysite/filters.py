# import django_filters
# from django.forms import TextInput
# from django_filters import DateFilter, CharFilter, NumericRangeFilter
#
# from .models import Post
#
#
# class TitleSearch(django_filters.FilterSet):
#     title = CharFilter(field_name='title', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'جستجو'}))
#
#     class Meta:
#         model = Post
#         fields = ['title']
#
#
# class AsideFilter(django_filters.FilterSet):
#     start_date = DateFilter(field_name='published_date', lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'بعد از تاریخ...'}))
#     end_date = DateFilter(field_name='published_date', lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'قبل از تاریخ...'}))
#     view = NumericRangeFilter(field_name='views', lookup_expr='lte')
#     title = CharFilter(field_name='title', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'جستجو'}))
#
#     class Meta:
#         model = Post
#         fields = ['title', 'text', 'published_date', 'views', 'commentCount']
#         exclude = ['published_date']
