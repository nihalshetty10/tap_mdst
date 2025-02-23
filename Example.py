weather = input("Is the weather rainy, foggy or sunny")
#hi
weather.lower()
speed = int(input("What is speed of car?"))
if (weather == "rainy" or weather == "foggy") and (speed>70):
    print ("High chance of accident!")
else:
    print ("Low chance of accident!")

speeds = [30, 45, 65, 70, 85, 90]
count = 0
for i in speeds:
    if i > 60:
        count+=1
print(count)

accident_prob = {"morning": 0.1, "afternoon": 0.2, "night": 0.5}
time = input("What is the time of day(morning, afternoon or night)?")
time.lower()
if time=="morning":
    print(accident_prob["morning"])
elif time=="afternoon":
    print(accident_prob["afternoon"])
elif time=="night":
    print(accident_prob["night"])
else:
    print("Unknown time of day")
