from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'make', 'model', 'year',
                  'mpg', 'added', 'updated', 'owner')
        model = Car
