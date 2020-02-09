from django.db import models


# Create your models here.
class BasicModel(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    add_user = models.IntegerField(null=True)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.IntegerField(null=True)
    is_deleted = models.IntegerChoices('0', '1')
    objects = models.Manager

    class Meta:
        abstract = True
