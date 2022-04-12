# Weather api
## _Weather Forecast JSON_

![N|Solid](	https://cdn.weatherapi.com/v4/images/weatherapi_logo.png)

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
