from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CommissionType(models.Model):

    type_name = models.CharField(max_length=254, default='')
    price = models.IntegerField(default=0)
    preview_url = models.CharField(max_length=254, default='')
    completed_url = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.type_name


class Commission(models.Model):

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(CommissionType, null=True, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
