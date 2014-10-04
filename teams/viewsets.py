from rest_framework.viewsets import ModelViewSet
from . import models, permissions


class TeamViewSet(ModelViewSet):
    model = models.Team
    permission_classes = (permissions.IsOwnerPermission, )


class PlayerViewSet(ModelViewSet):
    model = models.Player
