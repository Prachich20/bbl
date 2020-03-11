import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
from django.urls import reverse
import pytest
from django.test import Client, TestCase
from profile.models import ADMIN
from mixer.backend.django import mixer


@pytest.mark.django_db
class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        client = Client()
        client.login(username=ADMIN[0], password=ADMIN[1])

    def test_player(self):
        player = 'player_1_Yankees'
        url = reverse('players:playerdetails', args=(player,))
        response = self.client.get(url, follow=True)
        assert response.status_code, 200

    def test_selected(self):
        url = reverse('players:calculate')
        response = self.client.get(url, follow=True)
        assert response.status_code, 200

    def test_create_players(self):
        player = mixer.blend('players.Players')
        assert player.create_players