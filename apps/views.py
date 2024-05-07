from rest_framework.generics import ListCreateAPIView

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


class ProductCreateListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryCreateListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


