import settings
from django.db import models
from django.contrib.auth.models import User

ADMIN = (
    settings.ADMIN_USER,
    settings.ADMIN_PASS
)

ROLE = (
    ('0', 'Admin'),
    ('1', 'Coach'),
    ('2', 'Player'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE, default='2', max_length=6)

    class Meta:
        sorted('role')

    def __str__(self):
        return '{}'.format(self.role)

    def add_user(self, player):
        user = User()
        user.username = player.name
        user.set_password(settings.DEFAULT_PASSWORD)
        user.is_staff = True
        user.save()

        new_user = User.objects.filter(username=player.name).first()
        self.user = new_user
        self.role = '2' if player.coach is False else '1'
        self.save()
