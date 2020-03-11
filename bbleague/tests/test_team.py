import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
from django.urls import reverse
import pytest
from django.test import Client, TestCase
from profile.models import ADMIN
from team.models import Team
from mixer.backend.django import mixer


@pytest.mark.django_db
class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        client = Client()
        client.login(username=ADMIN[0], password=ADMIN[1])

    def test_team(self):
        team = 'Mets'
        url = reverse('team:teamdetails', args=(team,))
        response = self.client.get(url, follow=True)
        assert response.status_code, 200

    def test_create_team(self):
        team = mixer.blend(Team)
        Team().create_team(name=team.name)
        new_Team = Team.objects.filter(name=team.name).first()
        assert new_Team.name == team.name
