def autumn_weather():
    print("No leaves")
    print("Mild cold")

def spring_weather():
    print("Lots of colourful leaves")
    print("Warm weather")

weather=input("What weather is it?")
if weather=="autumn":
    autumn_weather()
else:
    spring_weather()
