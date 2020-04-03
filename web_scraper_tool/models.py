from django.db import models
import jsonfield
# Create your models here.


class ScrapData(models.Model):
    main_url = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    links = jsonfield.JSONField()
