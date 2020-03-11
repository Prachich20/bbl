import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
import pytest
from django.test import Client, TestCase
from profile.models import ADMIN
from django.urls import reverse
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
        game = mixer.blend('game.Game')
        assert game.create_game
