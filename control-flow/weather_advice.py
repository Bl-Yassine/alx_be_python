#Weather Recommendation Program
weather_to_day = str(input("What's the weather like today? (sunny/rainy/cold):"))

if weather_to_day == "sunny" :
    print("Wear a t-shirt and sunglasses.")
elif weather_to_day == "rainy" :
    print("Don't forget your umbrella and a raincoat.")
elif weather_to_day == "cold" :
    print("Make sure to wear a warm coat and a scarf.")
else :
    print("Sorry, I don't have recommendations for this weather.")
