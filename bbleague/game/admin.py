from django.contrib import admin
from game.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'round', 'winner', 'team1', 'team2', 'is_final')


admin.site.register(Game, GameAdmin)
