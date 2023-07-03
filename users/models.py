from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(BaseModel, AbstractUser):
    first_name = None
    last_name = None

    def get_full_name(self):
        return f'{self.username} - {self.email}'

    def get_short_name(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass
