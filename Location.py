from Api import location


class Location:

    def __init__(self, name, region, country, lat, lon, tz_id):
        """
        :param name: string	 Location name
        :param region: string	Region or state of the location, if available
        :param country: string	Location country
        :param lat: decimal	 Latitude in decimal degree
        :param lon: decimal	 Longitude in decimal degree
        :param tz_id: string  Continentul
        """
        self.name = name
        self.region = region
        self.country = country
        self.lat = lat
        self.lon = lon
        self.tz_id = tz_id

    def afisare(self, name):
        with open(f"{name}.txt", "w", errors="ignore") as file:
            file.write(f"Locatia {self.name}\n\n"
                       f"     Orasul {self.region}\n"
                       f"     Tara {self.country}\n"
                       f"     Latitudinea {self.lat}\n"
                       f"     Longitudinea {self.lon}\n"
                       f"     Zona Geografica {self.tz_id}\n\n")

    def returnare_nume(self):
        return self.name


class Current_day:
    def __init__(self, date, maxtemp_c, mintemp_c, avgtemp_c, totalprecip_mm, avgvis_km, condition_date, uv, sunrise,
                 sunset, moonrise, moonset, moon_phase):
        """

        :param date: string Data
        :param maxtemp_c: string Temperatura maxima
        :param mintemp_c: string Temperatura minima
        :param avgtemp_c: string Temperatura medie
        :param totalprecip_mm: string Preciptii totale
        :param avgvis_km: string Media vantului
        :param condition_date: string Conditii meteo
        :param uv: string condition_date
        :param sunrise: string Soarele rasare la ora
        :param sunset: string Soarele apune la ora
        :param moonrise: string Luna rasare la ora
        :param moonset: string Luna apune la ora
        :param moon_phase: string Fazele lunii
        """

        self.date = date
        self.maxtemp_c = maxtemp_c
        self.mintemp_c = mintemp_c
        self.avgtemp_c = avgtemp_c
        self.totalprecip_mm = totalprecip_mm
        self.avgvis_km = avgvis_km
        self.condition_date = condition_date
        self.uv = uv
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonrise = moonrise
        self.moonset = moonset
        self.moon_phase = moon_phase

    def afisare_location_info(self, name):
        with open(f"{name}.txt", "a", errors="ignore") as file:
            file.write(f"Istoria zilei {self.date}\n"
                       f"     Temperatura maxima {self.maxtemp_c} grade Celsius\n"
                       f"     Temperatura minima {self.mintemp_c} grade Celsius\n"
                       f"     Temperatura medie {self.avgtemp_c} grade Celsius\n"
                       f"     Preciptii totale {self.totalprecip_mm} mm\n"
                       f"     Media vantului {self.avgvis_km} km\ora\n"
                       f"     Conditii meteo {self.condition_date} mb\n"
                       f"     UV {self.uv}\n\n"
                       f"     Soarele rasare la ora {self.sunrise}\n"
                       f"     Soarele apune la ora {self.sunset}\n"
                       f"     Luna rasare la ora {self.moonrise}\n"
                       f"     Luna apune la ora {self.moonset}\n"
                       f"     Fazele lunii {self.moon_phase}\n\n\n")


class Current:
    def __init__(self, name, last_updated, temp_c, condition, wind_mph, win_dir, pressure_mb, precip_mm, humidity):
        """

        :param name: string	 Location name
        :param last_updated: string  Local date and time
        :param temp_c: float  Temperatura in grade Celsius
        :param wind_mph: float  Viteza vantului in mph
        :param win_dir: string  Directia vantului
        :param pressure_mb: float  Presiunea atmosferica in mb
        :param precip_mm: float  Precipitatii in mm
        :param humidity: int  Umiditatea
        """

        self.name = name
        self.last_update = last_updated
        self.temp_c = temp_c
        self.condition = condition
        self.wind_mph = wind_mph
        self.win_dir = win_dir
        self.pressure_mb = pressure_mb
        self.precip_mm = precip_mm
        self.humidity = humidity

    def afisare_location(self, name):
        with open(f"{name}.txt", "a", errors="ignore") as file:
            file.write(f"     Data si Ora {self.last_update}\n\n"
                       f"     Temperatura {self.temp_c} grade Celsius\n"
                       f"     Conditii {self.condition}\n"
                       f"     Viteza Vantului {self.wind_mph} mph\n"
                       f"     Directia Vantului {self.win_dir}\n"
                       f"     Presiunea Atmosferica {self.pressure_mb} mb\n"
                       f"     Precipitatii {self.precip_mm} mm\n"
                       f"     Umiditatea {self.humidity} %\n\n")


class Air:
    def __init__(self, name, co, no2, o3, so2, pm2_5, pm10, us_epa_index, gb_defra_index):
        """

        :param name: string	 Location name
        :param co: float  Carbon Monoxide (μg/m3)
        :param no2: float  Nitrogen dioxide (μg/m3)
        :param o3: float  Ozone (μg/m3)
        :param so2: float  Sulphur dioxide (μg/m3)
        :param pm2_5: float  PM2.5 (μg/m3)
        :param pm10: float  PM10 (μg/m3)
        :param us_epa_index: integer  US - EPA standard.
            1 means Good
            2 means Moderate
            3 means Unhealthy for sensitive group
            4 means Unhealthy
            5 means Very Unhealthy
            6 means Hazardous
        :param gb_defra_index: integer	UK Defra Index (See table below)

        """

        self.name = name
        self.co = co
        self.no2 = no2
        self.o3 = o3
        self.so2 = so2
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.us_epa_index = us_epa_index
        self.gb_defra_index = gb_defra_index

    def afisare_air_quality(self, name):
        with open(f"{name}.txt", "a", errors="ignore") as file:
            file.write(f"Calitatea Aerului: \n\n"
                       f"     Carbon Monoxide (μg/m3){self.co} μg/m3\n"
                       f"     Nitrogen dioxide {self.no2} μg/m3\n"
                       f"     Ozone {self.o3} μg/m3 \n"
                       f"     Sulphur dioxide {self.so2} μg/m3\n"
                       f"     PM2.5 {self.pm2_5} μg/m3\n"
                       f"     PM2.5 {self.pm10} μg/m3\n"
                       f"     US - EPA standard {self.us_epa_index}\n"
                       f"     UK Defra Index {self.gb_defra_index}\n"
                       f"                           See table below:\n"
                       f"                                           1 means Good\n"
                       f"                                           2 means Moderate\n"
                       f"                                           3 means Unhealthy for sensitive group\n"
                       f"                                           4 means Unhealthy\n"
                       f"                                           5 means Very Unhealthy\n"
                       f"                                           6 means Hazardous\n\n")


class Alert:

    def __init__(self, headline, severity, urgency, areas, event, effective, expires, desc):
        """

        :param name: string Numele Locatiei
        :param headline: string Zone Alertei
        :param severity: string Severitate
        :param urgency: string Urgenta
        :param areas: string Zona
        :param event: string Evenimentul
        :param effective: string Data inceperi alertei
        :param expires: string Data expirarii Alertei
        :param desc: string Descrierea Alertei
        """

        self.headline = headline
        self.severity = severity
        self.urgency = urgency
        self.areas = areas
        self.event = event
        self.effective = effective
        self.expires = expires
        self.desc = desc

    def afisare_info_alerts(self):
        with open(f"{location}.txt", "a", errors="ignore") as file:
            file.write(f"Alerte\n\n"f"     Titlul {self.headline}\n"
                       f"     Data inceperii {self.effective}\n"
                       f"     Severitate {self.severity}\n"
                       f"     Urgenta {self.urgency}\n"
                       f"     Zona {self.areas}\n"
                       f"     Evenimentul {self.event}\n"
                       f"     Data expirarii {self.expires}\n"
                       f"     Descrierea {self.desc}\n\n\n")
