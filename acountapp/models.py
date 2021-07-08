from django.db import models

# Create your models here.

class Content(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    text = models.CharField(max_length=255, null=False)
    # user_id = models.ForeignKey(to_field=id, db_column=)

# class UserAccount(models.Model):
#     id = models.CharField(max_length= 100, primary_key=True)
#     name = models.CharField(max_length=200, null=False)
