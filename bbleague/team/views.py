from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from players.models import Players
from team.models import Team
from tracking_analyzer.models import Tracker


@login_required
def teamdetails(request, team):
    team_name = Team.objects.filter(name=team).first()
    if team_name:
        players = Players.objects.filter(team=team_name)
        coach = players.filter(is_coach=True).first()

        if (coach and str(coach.name).strip() == str(request.user).strip()) or (request.user.is_superuser == True):
            context = {
                "team": team_name,
                "players": players,
                "coach": coach.name if coach else None,
            }
        else:
            context = {
                "error": "You cannot view this team details. Only coach and admin can view details for other teams."
            }
        Tracker.objects.create_from_request(request, request.user)
        return render(request, "teamdetails.html", context=context)
    else:
        context = {
            "error": "No team name %s exists" % team
        }
        return render(request, "teamdetails.html", context=context)
