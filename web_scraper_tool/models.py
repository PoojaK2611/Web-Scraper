from django.db import models
import jsonfield
# Create your models here.

class ScrapData(models.Model):
    phone = models.TextField()
    email = models.EmailField()
    data = jsonfield.JSONField()
