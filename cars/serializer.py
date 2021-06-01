from rest_framework import serializers
from cars.models import Car, CarSpecifications


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['carCode', 'carModel', 'manufacturingDate']


class CarSpecificationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarSpecifications
        fields = '__all__'
