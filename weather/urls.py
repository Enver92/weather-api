from django.urls import path

from .views import WeatherCreateAPIView

urlpatterns = [
    path("city", WeatherCreateAPIView.as_view()),
]
