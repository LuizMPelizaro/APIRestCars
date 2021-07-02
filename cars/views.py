from rest_framework import viewsets, generics
from cars.models import Car, CarSpecifications, Race
from cars.serializer import CarSerializer, RacesSerializer, CarSpecificationsSerializers, ListRacesSerializer, \
    ListCarPerRaceSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CarsViewSets(viewsets.ModelViewSet):
    """Show all cars"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    http_method_names = ['get', 'post', 'put','path']
    authentication_classes = [BasicAuthentication]
    IsAuthenticated = [IsAuthenticated]


class CarsSpecificationsViewSets(viewsets.ModelViewSet):
    """Show all specification of cars"""
    queryset = CarSpecifications.objects.all()
    serializer_class = CarSpecificationsSerializers
    http_method_names = ['get', 'post', 'put', 'path']
    authentication_classes = [BasicAuthentication]
    IsAuthenticated = [IsAuthenticated]


class RacesViewSets(viewsets.ModelViewSet):
    """Shows all races the car is entered"""
    queryset = Race.objects.all()
    serializer_class = RacesSerializer
    authentication_classes = [BasicAuthentication]
    IsAuthenticated = [IsAuthenticated]


class ListRacers(generics.ListAPIView):
    """Show all races of car"""

    def get_queryset(self):
        queryset = Race.objects.filter(car_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListRacesSerializer
    authentication_classes = [BasicAuthentication]
    IsAuthenticated = [IsAuthenticated]


class ListCarPerRace(generics.ListAPIView):
    """
    Show all car in race
    """

    def get_queryset(self):
        queryset = Race.objects.filter(race_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListCarPerRaceSerializer
    authentication_classes = [BasicAuthentication]
    IsAuthenticated = [IsAuthenticated]
