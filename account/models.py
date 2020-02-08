from django.db import models

from basic.models import BasicModel


class User(BasicModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField
    phone = models.CharField(max_length=50)
    is_admin = models.IntegerChoices('0', '1')

    @property
    def username(self):
        return '%s %s'.format(self.first_name, self.last_name)


class UserDetail(User):
    user_id = models.IntegerField(null=False)
    address = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
