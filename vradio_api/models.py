from django.db import models

# Create your models here.
class Type(models.Model):
  code = models.CharField(max_length = 10)
  img_path = models.CharField(max_length = 255)
  sex = models.CharField(max_length = 2)
  class Meta:
    db_table = 'types'

class Vtuber(models.Model):
  name = models.CharField(max_length = 50)
  channel_id = models.CharField(max_length = 255,null = True)
  chara_img = models.CharField(max_length = 255,null = True)
  company = models.CharField(max_length = 20,null = True)
  color = models.CharField(max_length = 8,default = '#ffffff')
  type = models.ForeignKey(Type, on_delete=models.CASCADE)
  class Meta:
    db_table = 'vtubers'
