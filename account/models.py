from django.db import models


class BasicModel(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    add_user = models.IntegerField(null=True)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.IntegerField(null=True)
    is_deleted = models.IntegerField(choices=('0', '1'), null=True)

    class Meta:
        abstract = True


class User(BasicModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField
    phone = models.CharField(max_length=50)
    is_admin = models.IntegerField(choices=('0', '1'))

    @property
    def username(self):
        return '%s %s'.format(self.first_name, self.last_name)


class UserDetail(User):
    user_id = models.IntegerField(null=False)
    address = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
