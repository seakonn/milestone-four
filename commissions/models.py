from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CommissionType(models.Model):
    """
    Model represents a type of commission (eg. statue, painting)
    Type is represented by a preview image and a completed image
    (from their respective urls)
    """

    type_name = models.CharField(max_length=254, default='')
    price = models.IntegerField(default=0)
    preview_url = models.CharField(max_length=254, default='')
    completed_url = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.type_name


class Commission(models.Model):
    """
    Model represents an art commission associated with a user
    and a particular type (see above)
    """

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(
        CommissionType, null=True, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
