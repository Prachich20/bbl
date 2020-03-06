from django.db import models
from team.models import Team

ROUND = (
    ('0', 'Round_0'),
    ('1', 'Round_1'),
    ('2', 'Round_2'),
    ('3', 'Round_3'),
    ('4', 'Round_4'),
)


class Game(models.Model):
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)

    round = models.CharField(choices=ROUND, default='0', max_length=1)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Team2')
    is_final = models.BooleanField(default=False)

    class Meta:
        sorted('round')

    def __str__(self):
        return '{}'.format(self.id)

    def create_game(self, winner, round, team1, team2, is_final):
        winning_team = Team.objects.filter(id=winner).first()
        team1_participant = Team.objects.filter(id=team1).first()
        team2_participant = Team.objects.filter(id=team2).first()
        self.winner = winning_team
        self.round = round
        self.team1 = team1_participant
        self.team2 = team2_participant
        self.is_final = is_final
        self.save()

        if is_final:
            team = Team.objects.all()
            for record in team:
                if record.id == winner:
                    record.is_winner = True
                else:
                    record.is_winner = False
                record.save()
