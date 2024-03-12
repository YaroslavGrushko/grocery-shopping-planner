import django_filters

class ProductFilter(django_filters.FilterSet):
    # Filter by foreign key
    category_id = django_filters.NumberFilter(field_name="category__id")