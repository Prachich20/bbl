import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
import pytest
from django.test import Client, TestCase
from django.urls import reverse
from profile.models import ADMIN
from game.models import Game
from mixer.backend.django import mixer


@pytest.mark.django_db
class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        client = Client()
        client.login(username=ADMIN[0], password=ADMIN[1])

    def test_game(self):
        url = reverse('game:index')
        response = self.client.get(url, follow=True)
        assert response.status_code, 200

    def test_logout(self):
        url = reverse('game:logout')
        response = self.client.get(url, follow=True)
        assert response.status_code, 200

    def test_create_game(self):
        game = mixer.blend(Game)
        Game().create_game(game.winner_id, game.round, game.team1_id, game.team2_id, game.is_final)
        new_game = Game.objects.filter(winner=game.winner, team1=game.team1, is_final=game.is_final).first()
        assert game.is_final == new_game.is_final
        assert game.winner == new_game.winner
