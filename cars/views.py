from rest_framework import viewsets
from cars.models import Car, CarSpecifications
from cars.serializer import CarSerializer, CarSpecificationsSerializers


class CarsViewSets(viewsets.ModelViewSet):
    """Show all cars"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsSpecificationsViewSets(viewsets.ModelViewSet):
    """Show all specification of cars"""
    queryset = CarSpecifications.objects.all()
    serializer_class = CarSpecificationsSerializers
