from django.db import models

from basic.models import BasicModel


class User(BasicModel):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50)
    salt = models.CharField(max_length=5,default=None)

    @property
    def username(self):
        return '%s %s'.format(self.first_name, self.last_name)


class UserDetail(User):
    user_id = models.IntegerField(null=False)
    address = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
