from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    average_score = models.IntegerField(default=0)
    is_winner = models.BooleanField(default=False)

    class Meta:
        sorted('name')

    def __str__(self):
        return '{}'.format(self.name)

    def create_team(self, name):
        team = Team.objects.filter(name=name).first()
        if not team:
            self.name = name
            self.save()
