import requests

from rest_framework.generics import CreateAPIView

from .models import Weather
from .serializers import WeatherSerializer

class WeatherCreateAPIView(CreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
