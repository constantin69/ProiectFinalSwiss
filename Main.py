from Api import response, location, numar, clear_console, introduce_location, introduce_limba, introduce_numar, Api
from Forescast import info_forecast, info_forecast_info
from Crearecsv import creare_csv, afisare_grafic
from Program import citire_location, citire_current, citire_air_quality
from Alerts import afisare_alerts
from search import sortare

response = response

while True:
    x = int(input(f"1: Informatii despre {location}\n2: Prognoza Meteo pe urmatoarele {numar} zile\n3: Alerte "
                  f"Meteo\n4: Introduceti o alta locatie\n 0: Terminare\n"))
    if x == 1:
        citire_location()
        citire_current()
        citire_air_quality()
        info_forecast_info(location)
        clear_console()
        continue

    if x == 2:
        my_list = info_forecast()
        creare_csv(my_list, location)
        afisare_grafic(location)
        clear_console()
        continue

    if x == 3:
        alerts = response["alerts"]["alert"]
        afisare_alerts(alerts)
        clear_console()
        continue

    if x == 4:
        location = input("Introduceti un oras in limba Engleza: ")
        lim = input("Alegeti limba: ")
        limba = sortare(lim)
        numar = int(input("Pentru prognoza meteo alegeti un numar de zile (1 - 3): "))
        a = Api(location, numar, limba)
        response = a.get_location()
        clear_console()
        continue

    if x == 0:
        exit()

    break
