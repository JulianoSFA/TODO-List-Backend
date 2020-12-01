from django.db import models

# Create your models here.

class ListItem(models.Model):
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=100, default='')
    dateTime = models.DateTimeField(auto_now_add=True)
    listItem = models.Manager()