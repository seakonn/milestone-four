from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Commission(models.Model):

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
