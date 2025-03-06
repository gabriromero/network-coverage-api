from rest_framework.routers import DefaultRouter

from network_coverage.views.network_coverage import CoverageViewSet

router = DefaultRouter()
router.register(r'', CoverageViewSet, basename='my-viewset')

urlpatterns = router.urls