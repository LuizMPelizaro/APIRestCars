from django.db import models


class Car(models.Model):
    carCode = models.CharField(max_length=9)
    carModel = models.CharField(max_length=50)
    manufacturingDate = models.DateField()

    def __str__(self):
        return self.carModel


class CarSpecifications(models.Model):
    CATEGORY = (
        ('F', 'Formula'),
        ('E', 'Endurance'),
        ('G', 'GT')
    )
    typeCar = models.CharField(max_length=20)
    typeEngine = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=1, choices=CATEGORY, blank=False, null=False, default='F')

    def __str__(self):
        return self.description


class Race(models.Model):
    TYPERACE = (
        ('L', 'Laps'),
        ('T', 'Time')
    )
    trackName = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    category = models.ForeignKey(CarSpecifications, on_delete=models.CASCADE)
    typeRace = models.CharField(max_length=1, choices=TYPERACE, blank=False, null=False, default='L')

