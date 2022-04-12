from Api import location, numar, response
from Location import Current_day

res = response
location = location
numar = numar

forecast = res["forecast"]["forecastday"]
my_list = list()
my_list_info = list()


def info_forecast():
    for nr in range(numar):

        hour = forecast[nr]["hour"]

        for i in hour:
            time = i["time"].split()
            my_dict = dict()
            my_dict["date"] = time[0]
            my_dict["hour"] = time[1]
            my_dict["temp_c"] = i["temp_c"]
            my_dict["condition"] = i["condition"]["text"]
            my_dict["wind_mph"] = i["wind_mph"]
            my_dict["wind_dir"] = i["wind_dir"]
            my_dict["pressure_mb"] = i["pressure_mb"]
            my_dict["precip_mm"] = i["precip_mm"]
            my_dict["humidity"] = i["humidity"]
            my_dict["uv"] = i["uv"]

            my_list.append(my_dict)

    return my_list


def info_forecast_info(name):
    date = forecast[0]["date"]
    maxtemp_c = forecast[0]["day"]["maxtemp_c"]
    mintemp_c = forecast[0]["day"]["mintemp_c"]
    avgtemp_c = forecast[0]["day"]["avgtemp_c"]
    totalprecip_mm = forecast[0]["day"]["totalprecip_mm"]
    avgvis_km = forecast[0]["day"]["avgvis_km"]
    condition_date = forecast[0]["day"]["condition"]["text"]
    uv = forecast[0]["day"]["uv"]
    sunrise = forecast[0]["astro"]["sunrise"]
    sunset = forecast[0]["astro"]["sunset"]
    moonrise = forecast[0]["astro"]["moonrise"]
    moonset = forecast[0]["astro"]["moonset"]
    moon_phase = forecast[0]["astro"]["moon_phase"]


    current_day = Current_day(date, maxtemp_c, mintemp_c, avgtemp_c, totalprecip_mm, avgvis_km, condition_date, uv,
                              sunrise, sunset, moonrise, moonset, moon_phase)
    current_day.afisare_location_info(name)


