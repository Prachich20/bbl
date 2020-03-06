from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Game
from team.models import Team
from tracking_analyzer.models import Tracker

@login_required
def index(request):
    games = Game.objects.all()
    teams = Team.objects.all().order_by('-average_score')
    context = {
        "games": games,
        "teams": teams,
    }
    Tracker.objects.create_from_request(request, request.user)
    return render(request, "home.html", context)


def logout(request):
    return render(request, "")