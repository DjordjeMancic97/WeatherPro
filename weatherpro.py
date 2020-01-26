import requests
from requests.exceptions import ConnectionError, HTTPError

print("""
    .%%...%%..%%%%%%...%%%%...%%%%%%..%%..%%..%%%%%%..%%%%%...%%%%%...%%%%%....%%%%..
    .%%...%%..%%......%%..%%....%%....%%..%%..%%......%%..%%..%%..%%..%%..%%..%%..%%.
    .%%.%.%%..%%%%....%%%%%%....%%....%%%%%%..%%%%....%%%%%...%%%%%...%%%%%...%%..%%.
    .%%%%%%%..%%......%%..%%....%%....%%..%%..%%......%%..%%..%%......%%..%%..%%..%%.
    ..%%.%%...%%%%%%..%%..%%....%%....%%..%%..%%%%%%..%%..%%..%%......%%..%%...%%%%..
    .................................................................................
                                                    made by Djordje Mancic, 2019 (c)
    """)

class GetWeather:
    
    # takes city name and returns latitude and longitude
    def locationData(self, cityName):
                locationApi = "get your own api key"
                locationUrl = "https://us1.locationiq.com/v1/search.php?key={}&q={}&format=json".format(locationApi, cityName)
                locationData = requests.get(locationUrl).json()
                lat = locationData[0]["lat"]
                lon = locationData[0]["lon"]
                showCity = locationData[0]["display_name"]
                return lat, lon, showCity
    
    # takes latitude and longitude and give weather data
    def darkSkyData(self, cityName, units):
            lat, lon, showCity = self.locationData(cityName)
            weatherApi = "get your own api key"
            weatherUrl = "https://api.darksky.net/forecast/{}/{},{}?units={}".format(weatherApi, lat, lon, units)
            weatherData = requests.get(weatherUrl).json()
            return weatherData, units, showCity

    # takes weather data and prints out nicely formated results
    def showWeather(self, weatherData, units):
            days = ["Today", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            weatherData, units, showCity = self.darkSkyData(weatherData, units)

            if(units == "us"):
                flags = "°F"
            elif(units == "si"):
                flags = "°C"

            # currently
            print("\n    *** LOCATION ***\n"
                "    {}\n"
                "\n    <<<Today>>>\n"
                "\n    Summary: {}\n"
                "    Currently: {}{}\n"
                "    Feels like: {}{}\n"
                "    High: {}{}\n"
                "    Low: {}{}\n"
                .format(showCity, weatherData["currently"]["summary"],
                round(weatherData["currently"]["temperature"]),flags,
                round(weatherData["currently"]["apparentTemperature"]), flags,
                round(weatherData["daily"]["data"][0]["temperatureHigh"]), flags,
                round(weatherData["daily"]["data"][0]["temperatureLow"]), flags))
            print("\n    <<<This week>>>\n"
                "\n    Summary: {}".format(weatherData["daily"]["summary"]))
            
            # weekly
            for day, weatherDay in zip(days, weatherData["daily"]["data"]):
                # skip Today in weekly view
                if(weatherDay == weatherData["daily"]["data"][0] and day == "Today"):
                    continue
                
                print("\n    *{}*\n"
                    "    Summary: {}\n"
                    "    High: {}{}\n"
                    "    Low: {}{}".
                    format(day, weatherDay["summary"], round(weatherDay["temperatureHigh"]), flags,
                    round(weatherDay["temperatureLow"]), flags))
                    
# takes user input (city) and feeds it to showWeather
while(True):
    try:
        unitInput = input("\n    Would you like weather in Fahrenheit or Celsius? Enter F or C: ").upper()
        if(unitInput == "F"):
            userInput = input("\n    What's the weather in: ")
            newData = GetWeather().showWeather(userInput, "us")
            break
        elif(unitInput == "C"):
            userInput = input("\n    What's the weather in: ")
            newData = GetWeather().showWeather(userInput, "si")
            break
        else:
            print("\n    Invalid choice")
    # if user is offline
    except ConnectionError:
        print("\n    Please enable your internet connection and try again.")
    # if input is something weird
    except KeyError:
        print("\n    That's not a city, you probably just smashed your keyboard!")
