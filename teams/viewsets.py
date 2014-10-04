from rest_framework.viewsets import ModelViewSet
from . import models, permissions


class TeamViewSet(ModelViewSet):
    model = models.Team
    permission_classes = (permissions.IsOwnerPermission, )

    #Modificamos la query para devolver los registros del usuario.
    def filter_queryset(self, queryset):
        queryset = super(TeamViewSet, self).filter_queryset(queryset)
        return queryset.filter(owner=self.request.user)


class PlayerViewSet(ModelViewSet):
    model = models.Player
