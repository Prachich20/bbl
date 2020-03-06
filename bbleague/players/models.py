from django.db import transaction
from django.db import models

from team.models import Team
from profile.models import Profile


class Players(models.Model):
    team = models.ForeignKey(Team, related_name='team', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    height = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    is_coach = models.BooleanField(default=False)
    score = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        sorted('name')

    def __str__(self):
        return '{}'.format(self.name)

    @transaction.atomic
    def create_players(self, team,  name, coach, height, score=score):
        team_name = Team.objects.filter(name=team).first()
        player = Players.objects.filter(name=name, team=team_name).first()
        if not player:
            player = Players()

        player.team = team_name
        player.name = name
        player.score = score
        player.coach = coach
        player.height = height
        if coach is True:
            coach_exists = Players.objects.filter(team=team_name, is_coach=True).first()
            if coach_exists is not None:
                raise ValueError("Cannot have more than 1 coach in a team.")
            else:
                player.is_coach = coach
        player.save()
        Profile().add_user(player=player)
