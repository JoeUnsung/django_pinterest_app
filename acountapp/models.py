from django.db import models

# Create your models here.

class Content(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    text = models.CharField(max_length=255, null=False)
