from rest_framework.viewsets import ModelViewSet
from . import models


class TeamViewSet(ModelViewSet):
    model = models.Team
