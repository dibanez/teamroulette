from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, default=None, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team)

    def __str__(self):
        tpl = '{} ({})'
        args = self.name, self.team
        return tpl.format(*args)











