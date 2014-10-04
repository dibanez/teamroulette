from rest_framework.routers import DefaultRouter
from .viewsets import TeamViewSet


router = DefaultRouter()
router.register('teams', TeamViewSet)
urlpatterns = router.urls
