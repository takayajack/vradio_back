from django.db import models

# Create your models here.
class Vtuber(models.Model):
  name = models.CharField(max_length = 50)
  channel_id = models.CharField(max_length = 255)