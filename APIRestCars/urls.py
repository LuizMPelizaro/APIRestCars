from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cars.views import CarsViewSets, CarsSpecificationsViewSets

router = routers.DefaultRouter()
router.register('cars', CarsViewSets, basename='Car')
router.register('carsSpecification', CarsSpecificationsViewSets, basename='CarSpecifications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
