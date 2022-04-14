from Location import Location, Current, Air
from Api import response

res = response


def citire_location():
    name = res["location"]["name"]
    region = res["location"]["region"]
    country = res["location"]["country"]
    lat = res["location"]["lat"]
    lon = res["location"]["lon"]
    tz_id = res["location"]["tz_id"]

    location = Location(name, region, country, lat, lon, tz_id)
    location.afisare(name)


def citire_current():
    name = res["location"]["name"]
    last_updated = res["current"]["last_updated"]
    temp_c = res["current"]["temp_c"]
    temp_f = res["current"]["temp_f"]
    condition = res["current"]["condition"]["text"]
    wind_mph = res["current"]["wind_mph"]
    win_dir = res["current"]["wind_dir"]
    pressure_mb = res["current"]["pressure_mb"]
    precip_mm = res["current"]["precip_mm"]
    humidity = res["current"]["humidity"]

    current = Current(name, last_updated, temp_c, condition, wind_mph, win_dir, pressure_mb, precip_mm, humidity)
    current.afisare_location(name)


def citire_air_quality():
    name = res["location"]["name"]
    co = res["current"]["air_quality"]["co"]
    no2 = res["current"]["air_quality"]["no2"]
    o3 = res["current"]["air_quality"]["o3"]
    so2 = res["current"]["air_quality"]["so2"]
    pm2_5 = res["current"]["air_quality"]["pm2_5"]
    pm10 = res["current"]["air_quality"]["pm10"]
    us_epa_index = res["current"]["air_quality"]["us-epa-index"]
    gb_defra_index = res["current"]["air_quality"]["gb-defra-index"]

    air = Air(name, co, no2, o3, so2, pm2_5, pm10, us_epa_index, gb_defra_index)
    air.afisare_air_quality(name)
