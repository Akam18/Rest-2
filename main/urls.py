from rest_framework import routers
from .API import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('api/categories', CategoryViewSet, basename='category')
router.register('api/products', ProductViewSet, basename='product')

urlpatterns = router.urls