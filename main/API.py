from rest_framework import viewsets, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status

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

    def destroy(self, request, *args, **kwargs): # Функция удаления обьекта
        instance = self.get_object() # тут держится удаленный обьект
        self.perform_destroy()  # удаляет окончательно
        return Response(status=status.HTTP_204_NO_CONTENT) # Возвращает ответ В виде сообщении 'HTTP_204_NO_CONTENT'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer =self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)