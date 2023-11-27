from rest_framework import routers
from .api import LeadViewSet

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet,'leads')

urlpatterns = router.urls
