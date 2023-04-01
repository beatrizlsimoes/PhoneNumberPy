import requests
import phonenumbers

phone_number = "+351000000000"  # Replace with your phone number

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Determine the latitude and longitude of the phone number
geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(parsed_number)
response = requests.get(geocode_url)
if response.status_code == 200:
    try:
        result = response.json()["results"][0]
        lat = result["geometry"]["location"]["lat"]
        lng = result["geometry"]["location"]["lng"]
    except IndexError:
        print("Error: No location found for the phone number.")
        exit()
else:
    print("Error: Could not determine the location. HTTP status code {}".format(response.status_code))
    exit()

# Reverse geocode the latitude and longitude to obtain the specific address
reverse_geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(lat, lng)
response = requests.get(reverse_geocode_url)
if response.status_code == 200:
    try:
        result = response.json()["results"][0]
        address = result["formatted_address"]
        print("Address:", address)
    except IndexError:
        print("Error: No address found for the location.")
        exit()
else:
    print("Error: Could not determine the address. HTTP status code {}".format(response.status_code))
    exit()

