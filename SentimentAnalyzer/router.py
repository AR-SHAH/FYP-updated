from rest_framework import routers
from mainApp.viewset import ProductViewSet

router = routers.DefaultRouter()
router.register('', ProductViewSet, basename='employees')
