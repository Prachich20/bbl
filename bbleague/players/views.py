from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from players.models import Players
import numpy as np
from tracking_analyzer.models import Tracker


@login_required
def playerdetails(request, player):
    player_selected = Players.objects.filter(name=player).first()
    context = {
        "data": player_selected,
    }
    Tracker.objects.create_from_request(request, request.user)
    return render(request, "playerdetails.html", context=context)


@login_required
def calculate(request):
    queryset = Players.objects.filter(score__isnull=False)
    scores = []
    for s in queryset:
        scores.append(s.score)
    percentile_score = np.percentile(scores, 90)
    records = queryset.filter(score__gte=percentile_score).order_by('-score')
    context = {
        "filtered_players": records,
    }
    return render(request, "selected.html", context=context)