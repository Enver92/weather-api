import requests

from rest_framework import serializers

from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ("city", "description", "temp", "timestamp")
        read_only_fields = ("description", "temp", "timestamp")

    def create(self, validated_data):
        w = Weather(
            city=validated_data.get("city")
        )
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c4e326863862fb255de9d3a95d485d53'
        r = requests.get(url.format(w.city)).json()
        w.description = r["weather"][0]["description"]
        w.temp = r["main"]["temp"]
        w.save()
        return w
