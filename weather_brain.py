import requests, pyttsx3, pythoncom

class WeatherPro:

    # takes city name and returns latitude and longitude
    def get_locationData(self, cityName):
        locationApi = "8ff0ec755a4b49"
        locationUrl = f"https://us1.locationiq.com/v1/search.php?key={locationApi}&q={cityName}&format=json"
        locationData = requests.get(locationUrl).json()
        lat = locationData[0]["lat"]
        lon = locationData[0]["lon"]
        showCity = locationData[0]["display_name"]
        return lat, lon, showCity

    # takes latitude and longitude and give weather data
    def get_weatherData(self, cityName, units):
        lat, lon, showCity = self.get_locationData(cityName)
        weatherApi = "b17e2674e7c52ad7f257113c5e3e1af5"
        weatherUrl = f"https://api.darksky.net/forecast/{weatherApi}/{lat},{lon}?units={units}"
        weatherData = requests.get(weatherUrl).json()
        return weatherData, units, showCity

    # takes weather data and prints out nicely formated results
    def show_weather(self, weatherData, units, flags, flagsW):
        weatherData, units, showCity = self.get_weatherData(weatherData, units)

        #current vars
        current_summary = weatherData["currently"]["summary"]
        current_temp = round(weatherData["currently"]["temperature"])
        feels_like_temp = round(weatherData["currently"]["apparentTemperature"])
        high_temp = round(weatherData["daily"]["data"][0]["temperatureHigh"])
        low_temp = round(weatherData["daily"]["data"][0]["temperatureLow"])
        current_windspeed = round(weatherData["currently"]["windSpeed"])
        current_pressure = round(weatherData["currently"]["pressure"])
        current_uvindex = weatherData["currently"]["uvIndex"]

        print(f"""\n        *** LOCATION ***

        {showCity}

        *** TODAY ***

        Summary: {current_summary}
        Currently: {current_temp}{flags}
        Feels like: {feels_like_temp}{flags}
        High: {high_temp}{flags}
        Low: {low_temp}{flags}
        Wind speed: {current_windspeed} {flagsW}
        Pressure: {current_pressure} mb
        UV index: {current_uvindex}
        """)
        
        #daily vars
        days = ["Today", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        daily_summary = weatherData["daily"]["summary"]
        daily_data = weatherData["daily"]["data"]

        print(f"""        *** THIS WEEK ***
        This week's summary: {daily_summary}\n""")

        for day, weatherDay in zip(days, daily_data):
            # skip Today in daily view
            if(weatherDay == weatherData["daily"]["data"][0] and day == "Today"):
                continue
            print(f"""        *{day}*

        Summary: {weatherDay["summary"]}
        High: {round(weatherDay["temperatureHigh"])}{flags}
        Low: {round(weatherDay["temperatureLow"])}{flags}
        Wind speed: {round(weatherDay["windSpeed"])}{flagsW}
        Pressure: {round(weatherDay["pressure"])} mb
        UV index: {weatherDay["uvIndex"]}
        """)

        return 0

    def quick_weather(self, weatherData, units, flags):
        weatherData, units, showCity = self.get_weatherData(weatherData, units)
        
        #tts data
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 140)
        
        
        # weather data
        current_summary = weatherData["currently"]["summary"]
        current_temp = round(weatherData["currently"]["temperature"])
        high_temp = round(weatherData["daily"]["data"][0]["temperatureHigh"])
        low_temp = round(weatherData["daily"]["data"][0]["temperatureLow"])
        weather_output = f"\n{showCity}.\n{current_summary}.\nCurrently it's {current_temp}{flags}. Highest temperature is {high_temp}{flags}, lowest is {low_temp}{flags}."
        
        print(weather_output)
        engine.say(weather_output)
        engine.runAndWait()
        return None