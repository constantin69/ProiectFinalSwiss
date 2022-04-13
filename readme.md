# Weather api
## _Weather Forecast JSON_

![N|Solid](	https://cdn.weatherapi.com/v4/images/weatherapi_logo.png)

1. Titlul proiectului
Weather api
Prognoza meteo JSON

Acesta este numele proiectului. Prin acest proiect am dorit sa arat modul in care este folosit un api, aici am folosit WeatherAPI.com. 
WeatherAPI.com este un puternic furnizor gratuit de API pentru vreme, care oferă API-uri extinse care variază de la prognoza meteo în timp real, vremea istorică, datele despre calitatea aerului, căutarea IP, fus orar și altele.
 
2. Descrierea proiectului

Adresa URL de baza pe care o folosesc in acest proiect este:
http://api.weatherapi.com/v1

Parametrii pe care i-am folosit in cadrul acestui URL sunt dati de la tastatura, acestia sunt:
Location 
Obiectul de locație este returnat cu fiecare răspuns API. Este de fapt locația potrivită pentru 
care au fost returnate informațiile.

Limba
Reprezinta limba care va fi folostita la afisarea informatiilor;

- numar = reprezinta numarul de zile pentru prognoza meteo.



Descrierea ta este un aspect extrem de important al proiectului tau. O descriere bine realizată vă permite să vă prezentați munca altor dezvoltatori, precum și potențialilor angajatori.

Calitatea unei descrieri README diferențiază adesea un proiect bun de un proiect prost. Unul bun profită de oportunitatea pentru a explica și prezenta:

    Ce face aplicația dvs.,
    De ce ați folosit tehnologiile pe care le-ați folosit,
    Unele dintre provocările cu care te-ai confruntat și funcții pe care speri să le implementezi în viitor.

3. Cuprins (Opțional)

Dacă README-ul dvs. este foarte lung, este posibil să doriți să adăugați un cuprins pentru a facilita navigarea cu ușurință a utilizatorilor la diferite secțiuni. Va fi mai ușor pentru cititori să se deplaseze cu ușurință prin proiect.
4. Cum se instalează și se rulează proiectul

Dacă lucrați la un proiect pe care un utilizator trebuie să-l instaleze sau să ruleze local într-o mașină precum un „POS”, ar trebui să includeți pașii necesari pentru a vă instala proiectul și, de asemenea, dependențele necesare, dacă există.

Furnizați o descriere pas cu pas a modului de setare și de funcționare a mediului de dezvoltare.
5. Cum se utilizează proiectul

Furnizați instrucțiuni și exemple pentru ca utilizatorii/contribuitorii să poată utiliza proiectul. Acest lucru le va face mai ușor în cazul în care întâmpină o problemă – vor avea întotdeauna un loc pentru a face referire la ceea ce se așteaptă.

De asemenea, puteți utiliza ajutoare vizuale incluzând materiale precum capturi de ecran pentru a afișa exemple ale proiectului în derulare și, de asemenea, structura și principiile de proiectare utilizate în proiectul dvs.

De asemenea, dacă proiectul dvs. va necesita autentificare, cum ar fi parole sau nume de utilizator, aceasta este o secțiune bună pentru a include acreditările.
6. Include credite

Dacă ați lucrat la proiect ca o echipă sau o organizație, enumerați colaboratorii/membrii echipei. De asemenea, ar trebui să includeți link-uri către profilurile lor GitHub și rețelele sociale.

De asemenea, dacă ați urmat tutoriale sau ați făcut referire la un anumit material care l-ar putea ajuta pe utilizator să construiască acel proiect anume, includeți și linkuri către cele de aici.

Acesta este doar o modalitate de a-ți arăta aprecierea și, de asemenea, de a-i ajuta pe alții să obțină o copie de primă mână a proiectului.
7. Adăugați o licență

Pentru majoritatea fișierelor README, aceasta este de obicei considerată ultima parte. Le permite altor dezvoltatori să știe ce pot și nu pot face cu proiectul dvs.

Avem diferite tipuri de licențe, în funcție de tipul de proiect la care lucrați. În funcție de cel pe care îl vei alege, acesta va determina contribuțiile pe care le primește proiectul tău.

Cea mai comună este Licența GPL, care permite altora să modifice codul dvs. și să-l folosească în scopuri comerciale. Dacă aveți nevoie de ajutor pentru a alege o licență, consultați acest link: https://choosealicense.com/

Până în acest moment, ceea ce am acoperit sunt cerințele minime pentru un bun README. Dar ar putea dori, de asemenea, să luați în considerare adăugarea următoarelor secțiuni pentru a o face mai atrăgătoare și mai interactivă.


WeatherAPI.com is a powerful fully managed free weather and geolocation API provider that provides extensive APIs that range from the realtime and weather forecast, historical weather, Air Quality Data, IP lookup, and astronomy through to sports, time zone, and geolocation.
WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy.

We provide following data through our API:

 * Real-time weather
 * 3 day weather forecast
 * Historical weather
 * Future Weather
 * Time zone
 * Location data
 * Search or Autocomplete API
 * Weather Alerts
 * Air Quality Data

## Getting Started

You need to signup and then you can find your API key under your account, and start using API right away!

## Authentication
API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.


Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .

key parameter
key=<YOUR API KEY>

## Request

Request URL
Request to WeatherAPI.com API consists of base url and API method. You can make both HTTP or HTTPS request to our API.

Base URL: http://api.weatherapi.com/v1


| API | API Method |
| ------ | ------ |
| Forecast | /forecast.json |

## Location Object

Location object is returned with each API response. It is actually the matched location for which the information has been returned.

It returns information about the location including geo points, name, region, country and time zone information as well.

| Field | Description |
| ------ | ------ |
| name | Location name |
| region | Region or state of the location |
| country | Location country |
| lat | Latitude in decimal degree |
| lon | Longitude in decimal degree |
| tz_id | Time zone name |


## Weather Alerts

Forecast API returns alerts and warnings issued by government agencies (USA, UK, Europe and Rest of the World) as an array if available for the location provided through the Forecast API.

By default alerts are not returned. To get alerts back in the response from Forecast API, pass the parameter alerts=yes.

##### Example response of alerts

"alerts":{
    "alert":[
        {
        "headline":"Flood Warning issued January 05 at 9:47PM EST until January 07 at 6:15AM EST by NWS",
        "msgtype":"Alert",
        "severity":"Moderate",
        "urgency":"Expected",
        "areas":"Calhoun; Lexington; Richland",
        "event":"Flood Warning",
        "effective":"2021-01-05T21:47:00-05:00",
        "expires":"2021-01-07T06:15:00-05:00",
        "desc":"...The Flood Warning continues for the following rivers in South\nCarolina...\nCongaree River At Carolina Eastman affecting Richland, Calhoun\nand Lexington Counties.\nCongaree River At Congaree National Park-Gadsden affecting\nCalhoun and Richland Counties.\nNorth Fork Edisto River At Orangeburg affecting Orangeburg County.\n...This crest compares to a previous crest of 116.3\nfeet on 12/03/2020.\n&&",
        },


## Air Quality Data

Air Quality data is returned in the Forecast API and Realtime API response. Depending upon your subscription plan we provide current and 3 day air quality data for the given location in json and xml.

It provides air quality index (see below) data on major pollutant gases like Carbon monoxide (CO), Ozone (O3), Nitrogen dioxide (NO2), Sulphur dioxide (SO2), PM 2.5 and PM 10.

By default air quality data is not returned. To get air quality data back in the response from Forecast API and Realtime API, pass the parameter aqi=yes.

| Field | Description |
| ------ | ------ |
| co | Carbon Monoxide (μg/m3) |
| o3 | Ozone (μg/m3) |
| no2 | Nitrogen dioxide (μg/m3) |
| so2 | Sulphur dioxide (μg/m3) |
| pm2_5 | PM2.5 (μg/m3) |
| pm10 | PM10 (μg/m3) |
| us-epa-index | US - EPA standard.
|              |1 means Good   |
|              |2 means Moderate|
|              |3 means Unhealthy for sensitive group|
|              |4 means Unhealthy|
|              |5 means Very Unhealthy|
|              |6 means Hazardous |
| gb-defra-index | UK Defra Index  |

## Realtime API

Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.
Current object contains current or realtime weather information for a given city.

| Field | Description |
| ------ | ------ |
| temp_c | Temperature in celsius |
| condition:text |Weather condition text |
| wind_mph | Wind speed in miles per hour |
| wind_kph | Wind speed in kilometer per hour |
| wind_dir | Wind direction as 16 point compass. e.g.: NSW |
| pressure_mb | Pressure in millibars |
| precip_mm | Precipitation amount in millimeters|
| humidity  |Humidity as percentage   |
| uv        |UV Index|
|              |3 means Unhealthy for sensitive group|
|              |4 means Unhealthy|
|              |5 means Very Unhealthy|
|              |6 means Hazardous |
| gb-defra-index | UK Defra Index  |


## Forecast API

Forecast weather API method returns upto next 10 day weather forecast and weather alert as json. The data is returned as a Forecast Object.


Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city.


forecastday: Parent element


forecastday -> day: 'day' element inside forecastday contains max/min temperature, average temperature


forecastday -> astro
forecastday -> hour:

| Forecastday | Parent element |
| ------ | ------ |
| forecastday -> day | day element contains:
|                    | * Max, min and average temperature
|                    | * Max wind speed
|                    | * Total precipitation
|                    | * Day weather conditionTemperature in celsius |
|forecastday -> astro |astro element contains sunrise, sunset, moonrise and moonset data |
| forecastday -> hour |hour element contains hour by hour weather forecast information |

#### forecastday

| Field | Description |
| ------ | ------ |
| date | Forecast date |
|day |See day element |
| astro | See astro element |
| hour | See hour element |

#### day Element

|Field	|	Description|
|-------|--------------|
|maxtemp_c|	Maximum temperature in celsius for the day|
|mintemp_c|	Minimum temperature in celsius for the day|
|avgtemp_c|	Average temperature in celsius for the day|
|maxwind_kph|Maximum wind speed in kilometer per hour|
|totalprecip_mm|Total precipitation in milimeter|
|condition:text|Weather condition text|
|uv|	decimal	UV Index|

#### astro Element
|Field|Type	Description|
|-----|----------------|
|sunrise|Sunrise time|
|sunset|Sunset time|
|moonrise|Moonrise time
|moonset|Moonset time|
|moon_phase|Moon phases.|

#### hour Element
|Field|	Description|
|-----|------------|
|time|Date and time|
|temp_c|Temperature in celsius|
|condition:text|Weather condition text|
|wind_kph|Maximum wind speed in kilometer per hour|
|wind_dir|Wind direction as 16 point compass. e.g.: NSW|
|pressure_mb|Pressure in millibars|
|precip_mm|Precipitation amount in millimeters|
|humidity|Humidity as percentage|

## Search API
WeatherAPI.com Search or Autocomplete API returns matching cities and towns as an array of Location object.
