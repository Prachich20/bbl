from django.contrib import admin
from team.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'average_score', 'is_winner')


admin.site.register(Team, TeamAdmin)
