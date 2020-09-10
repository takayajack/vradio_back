from rest_framework import serializers
from .models import Vtuber
from .models import Type
class TypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Type
    fields = ('code', 'img_path', 'sex')

class VtuberSerializer(serializers.ModelSerializer):
  type = TypeSerializer(read_only=True)
  class Meta:
    model = Vtuber
    fields = ('name', 'channel_id', 'chara_img', 'company', 'color', 'type')

