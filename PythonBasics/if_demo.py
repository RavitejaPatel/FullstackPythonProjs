india = ["hyderabad","delhi"]
USA = ["redmond", "seattle"]

city = input("enter the city:")
city=city.lower()

if city in india:
    print(f"{city.lower} from india")
elif city in USA:
    print(f"{city} from USA")
else:
    print(f"{city} from other country")