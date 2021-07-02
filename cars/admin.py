from django.contrib import admin

from cars.models import *


class Cars(admin.ModelAdmin):
    list_display = ('carCode', 'carModel', 'manufacturingDate')
    list_display_links = ('carCode', 'carModel')
    search_fields = ('carCode',)
    list_per_page = 20


admin.site.register(Car, Cars)


class CarsSpecifications(admin.ModelAdmin):
    list_display = ('id','typeCar', 'typeEngine', 'description')
    list_display_links = ('id', 'typeCar')
    search_fields = ('id', 'typeCar')
    list_per_page = 20


admin.site.register(CarSpecifications, CarsSpecifications)


class Races(admin.ModelAdmin):
    list_display = ('id', 'trackName', 'car', 'category')
    list_display_links = ('id', 'trackName',)


admin.site.register(Race, Races)

