from django.contrib import admin
from django.urls import path

from cars.views import cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars),
]
