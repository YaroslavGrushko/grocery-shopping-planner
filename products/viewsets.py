from rest_framework.viewsets import ModelViewSet

from products.models import Product, Category
from products.serializers import ProductSerializer, ProductViewSerializer, CategorySerializer

from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from products.filters import ProductFilter
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related("category")
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        try:
            current_user = self.request.user
            return self.queryset.filter(category__user=current_user)
        except:
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
    permission_classes = (IsAuthenticated,)

