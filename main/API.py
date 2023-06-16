from rest_framework import viewsets, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =[
        permissions.AllowAny, # Разрешение на все запросы
        # permissions.IsAuthenticated, # Разрешение после авторизации
        # permissions.IsAdminUser, # Разрешение только для администраторов
        # permissions.IsAuthenticatedOrReadOnly, # Разрешение на чтение без администратратора 
    ]


class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.AllowAny,
    ]