from rest_framework.viewsets import ModelViewSet
from . import models


class TeamViewSet(ModelViewSet):
    model = models.Team


class PlayerViewSet(ModelViewSet):
    model = models.Player
