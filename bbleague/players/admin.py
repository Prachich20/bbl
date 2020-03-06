from django.contrib import admin
from players.models import Players


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team', 'score', 'is_coach')


admin.site.register(Players, PlayersAdmin)
