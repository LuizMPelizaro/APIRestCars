from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cars.views import CarsViewSets, CarsSpecificationsViewSets, RacesViewSets, ListRacers

router = routers.DefaultRouter()
router.register('cars', CarsViewSets, basename='Car')
router.register('carsSpecification', CarsSpecificationsViewSets, basename='CarSpecifications')
router.register('races', RacesViewSets, basename='Race')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('car/<int:pk>/races/', ListRacers.as_view()),
    path('race/<int:pk>/cars', ListRacers.as_view())
]
