from django.shortcuts import render
from django.contrib.auth import authenticate
from tracking_analyzer.models import Tracker


def login(request, uname, pwd):
    user = authenticate(username=uname, password=pwd)
    if user is not None:
        Tracker.objects.create_from_request(request, user)
        request.user = user
        return render(request, "home.html", user)
    else:
        context = {
            "error": "Invalid username and password."
        }
        return render(request, "login.html", context)

