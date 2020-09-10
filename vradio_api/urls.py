from rest_framework import routers
from .views import VtuberViewSet,TypeViewSet

router = routers.DefaultRouter()
router.register(r'vtubers', VtuberViewSet)
router.register(r'Types',TypeViewSet)