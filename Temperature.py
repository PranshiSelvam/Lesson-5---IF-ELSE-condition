temperature = float(input("Enter the temperature in degrees Celsius: "))
if temperature >= 30:
    print("It's hot! Wear light clothing like shorts and a t-shirt.")
elif 20 <= temperature < 30:
    print("It's warm! A light jacket or shirt should be fine.")
elif 10 <= temperature < 20:
    print("It's a bit chilly! Wear a sweater or a light jacket.")
elif 0 <= temperature < 10:
    print("It's cold! Wear a heavy coat, scarf, and gloves.")
else:
    print("It's freezing! Bundle up with layers and a warm coat.") 

