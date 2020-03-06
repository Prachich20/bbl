import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from django.contrib.auth.models import User
import random
from random import randrange
from players.models import Players
from team.models import Team
from game.models import Game, ROUND
from profile.models import Profile, ADMIN

TEAM = ['knights', 'Pelicans', 'Rockers', 'Dodgers', 'Yankees', 'Bravers', 'Cardinals', 'Angels', 'Giants', 'Philies',
        'Cubs', 'Mets', 'Pirates', 'Jays', 'Mariners', 'Tigers']

teams = Team.objects.all()


# calculate average score for each team
def average_score():
    for team in teams:
        players = Players.objects.filter(team=team)
        average_score = 0
        for player in players:
            if player.score is not None:
                average_score = average_score + player.score
        team.average_score = average_score
        team.save(update_fields=['average_score'])


# assign mock score to each player in winning team
def assign_score(team):
    players = Players.objects.filter(team=team)
    for player in players:
        num = randrange(2, 10)
        if player.score is not None:
            player.score = player.score + num
            player.save(update_fields=['score'])


# randomly select qualifying teams for matches
def select_team(i, collection):
    team1 = list(collection)[i]
    team2 = list(collection)[len(collection) - 1 - i]
    return team1, team2


# create game records
def matches(data, round, is_final=False):
    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    winners = []
    for i in range(0, len(sorted_data) // 2):
        team1, team2 = select_team(i, sorted_data)
        won = random.choice([team1, team2])
        winners.append(won)

        # assign scores
        assign_score(won)

        Game().create_game(winner=team2, round=round, team1=team1, team2=team2, is_final=is_final)
    return winners


# get latest score after each match
def get_score(winners_qualifying, team_dict):
    qualifying = {}
    for team in winners_qualifying:
        for id, score in team_dict.items():
            if id == team:
                qualifying[id] = score
    return qualifying


# method to create superuser
def createadmin():
    user = User()
    user.username = ADMIN[0]
    user.set_password(ADMIN[1])
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()


# method to create team and all players
def createteam():
    for i in range(0, len(TEAM)):
        Team().create_team(name=TEAM[i])
        print("Team %s created successfully" % TEAM[i])
        for j in range(0, 11):
            name = "player_%s_%s" % (j, TEAM[i])
            coach = False
            height = float(randrange(60, 70) / 10)
            score = 0
            if j == 0:
                name = "coach_%s_%s" % (j, TEAM[i])
                coach = True
                score = None
            Players().create_players(team=TEAM[i], name=name, coach=coach, height=height,
                                     score=score)
        print("Players created successfully")


def load():
    Game.objects.all().delete()
    Team.objects.all().delete()
    User.objects.all().delete()
    Profile.objects.all().delete()

    createadmin()
    createteam()

    # leagues
    leagues = Team.objects.all()
    team_dict = {}
    for league in leagues:
        team_dict[league.id] = league.average_score

    winners_qualifying = matches(team_dict, round=ROUND[1][0])

    # quarter finals
    firstqualifying_dict = get_score(winners_qualifying, team_dict)
    winners_firstqualifying = matches(firstqualifying_dict, round=ROUND[2][0])

    # semifinals
    semiqualifying_dict = get_score(winners_firstqualifying, firstqualifying_dict)
    winners_semiqualifying = matches(semiqualifying_dict, round=ROUND[3][0])

    # finale
    finale_dict = get_score(winners_semiqualifying, semiqualifying_dict)
    finale_winner = matches(finale_dict, is_final=True, round=ROUND[4][0])

    # load average_score for team
    average_score()

    print("All games created successfully")


if __name__ == "__main__":
    load()
    print("Data load Completed !!!")
