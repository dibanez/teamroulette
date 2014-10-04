from rest_framework.viewsets import ModelViewSet
from . import models
from rest_framework.permissions import BasePermission

class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class TeamViewSet(ModelViewSet):
    model = models.Team
    permission_classes = IsOwnerPermission


class PlayerViewSet(ModelViewSet):
    model = models.Player
