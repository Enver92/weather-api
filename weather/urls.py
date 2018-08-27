from django.urls import path

from .views import WeatherCreateAPIView

urlpatterns = [
    path("", WeatherCreateAPIView.as_view()),
]
