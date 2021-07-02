from rest_framework import serializers
from cars.models import Car, CarSpecifications, Race


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarSpecificationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarSpecifications
        fields = '__all__'


class RacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        exclude = []


class ListRacesSerializer(serializers.ModelSerializer):
    carCode = serializers.ReadOnlyField(source='car.carCode')
    typeRace = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = Race
        fields = ['trackName', 'typeRace', 'carCode', 'category']

    def get_typeRace(self, obj):
        return obj.get_typeRace_display()


class ListCarPerRaceSerializer(serializers.ModelSerializer):
    carModel = serializers.ReadOnlyField(source='car.carModel')

    class Meta:
        model = Race
        fields = ['carModel']
