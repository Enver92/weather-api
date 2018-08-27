import requests

from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=30)
    temp = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    # def set_weather(self):
    #     print(self.city)
    #     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c4e326863862fb255de9d3a95d485d53'
    #     r = requests.get(url.format(self.city)).json()
    #     print(r)
    #     self.description = r["weather"][0]["description"]
    #     self.temp = r["main"]["temp"]

    def __str__(self):
        return "{}: {} degrees, {}".format(self.city, self.temp, self.description)
