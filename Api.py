import os
import requests
from search import sortare


def clear_console():
    os.system('cls')


clear_console()


def introduce_location():
    clear_console()
    location = input("Introduceti un oras in limba Engleza: ")
    return location


location = introduce_location()


def introduce_limba():
    print("Legenda limba:\n"
          "              Bulgarian\n"
          "              Arabic\n"
          "              Czech\n"
          "              Dutch\n"
          "              Finnish\n"
          "              French\n"
          "              German\n"
          "              Greek\n"
          "              Hungarian\n"
          "              Italian\n"
          "              Japanese\n"
          "              Polish\n"
          "              Portuguese\n"
          "              Romanian\n"
          "              Russian\n"
          "              Serbian\n"
          "              Slovak\n"
          "              Spanish\n"
          "              Swedish\n"
          "              Turkish\n")

    lim = input("Alegeti limba: ")
    limba = sortare(lim)
    return limba


limba = introduce_limba()


def introduce_numar():
    numar = int(input("Pentru prognoza meteo alegeti un numar de zile (1 - 3): "))
    return numar


numar = introduce_numar()

clear_console()


class Api:
    url = "http://api.weatherapi.com/v1/forecast.json"

    def __init__(self, location, numar, limba):
        self.location = location
        self.numar = numar
        self.limba = limba

    def get_location(self):
        params = {"q": location, "aqi": "yes", "days": numar, "alerts": "yes", "lang": limba, "hour": "yes",
                  "key": "a9eeceb06dd44e9eb3b143758220704"}
        resp = requests.request("GET", Api.url, params=params).json()
        return resp


api_obj = Api(location, numar, limba)
response = api_obj.get_location()
