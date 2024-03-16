from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category
from products.serializers import ProductSerializer, ProductViewSerializer, CategorySerializer

from django_filters.rest_framework import DjangoFilterBackend
from products.filters import ProductFilter
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related("category")
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        try:
            current_user = self.request.user
            return self.queryset.filter(category__user=current_user)
        except Exception:
            # not authorized user
            return None
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductViewSerializer
        else:
            return ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            current_user = self.request.user
            return self.queryset.filter(user=current_user)
        except Exception:
            # not authorized user
            return None

