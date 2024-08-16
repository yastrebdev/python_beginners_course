temp = input('What is the temperature outside?: ')
season = input("What's the season like now?: ") # summer or winter or autumn or spring

if not temp.isdigit():
    print("Enter a number")
elif season == 'autumn' or season == 'spring':
    print("Oh, it's too damp")
elif 0 < int(temp) <= 15 and season == "summer":
    print("It's cold outside")
elif 0 < int(temp) <= 15 and season == "winter":
    print("It's hot outside")
else:
    print("I can get out")

