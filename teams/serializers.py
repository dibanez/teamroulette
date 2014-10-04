from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=False)

    class Meta:
        model = models.Player
        fields = ('id', 'name', 'team')

