from django.db import models
from django.utils import timezone

# Create your models here.

class Subscription(models.Model):
        # name = models.CharField(max_length=100)
        email = models.EmailField(max_length = 100 , unique = True)
        date_created = models.DateTimeField( default = timezone.now )

        def __str__(self):
             return self.email