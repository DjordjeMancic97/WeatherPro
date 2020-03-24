from weather_brain import WeatherPro
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", help="C stands for Celsius and expects city name after. Example: python weatherpro.py -c Belgrade")
parser.add_argument("-f", help="F stands for Fahrenheit and expects city name after. Example: python weatherpro.py -f Belgrade")
args = parser.parse_args()

if args.c:
    try:
        quick = WeatherPro().quick_weather(args.c, "si", "°")
        
    except KeyError:
         print("That's not a city, you probably just smashed your keyboard!")
    except ConnectionError:
        print("Please enable your internet connection and try again.")
elif args.f:
    try:
        quick = WeatherPro().quick_weather(args.f, "us", "°")
        
    except KeyError:
        print("That's not a city, you probably just smashed your keyboard!")
    except ConnectionError:
        print("Please enable your internet connection and try again.")
else:   
    print("""
        .%%...%%..%%%%%%...%%%%...%%%%%%..%%..%%..%%%%%%..%%%%%...%%%%%...%%%%%....%%%%..
        .%%...%%..%%......%%..%%....%%....%%..%%..%%......%%..%%..%%..%%..%%..%%..%%..%%.
        .%%.%.%%..%%%%....%%%%%%....%%....%%%%%%..%%%%....%%%%%...%%%%%...%%%%%...%%..%%.
        .%%%%%%%..%%......%%..%%....%%....%%..%%..%%......%%..%%..%%......%%..%%..%%..%%.
        ..%%.%%...%%%%%%..%%..%%....%%....%%..%%..%%%%%%..%%..%%..%%......%%..%%...%%%%..
        .................................................................................
                                                        made by Djordje Mancic, 2019 (c)
        """)

    while(True):
        try:
            unitInput = input(
            "\n        Would you like weather in Fahrenheit or Celsius? Enter F or C: ").upper()
            if(unitInput == "F"):
                userInput = input("        What's the weather in: ")
                wProCurrent = WeatherPro().show_weather(userInput, "us", "°F", "mph")
                break
            elif(unitInput == "C"):
                userInput = input("        What's the weather in: ")
                wProCurrent = WeatherPro().show_weather(userInput, "si", "°C", "kph")
                break
            else:
                print("\nInvalid choice")
        except ConnectionError:
            print("\n        Please enable your internet connection and try again.")
        except KeyError:
            print("\n        That's not a city, you probably just smashed your keyboard!")
