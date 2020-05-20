from django.db import models


# Create your models here.
class Commission(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    #type = models.CharField(label='TEST LABEL', widget=models.Select(choices=COMMISSION_TYPES))

    #def __str__(self):
     #   return self.name