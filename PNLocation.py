import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = "+351000000000"  # Replace with your phone number

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Determine the carrier
carrier_name = carrier.name_for_number(parsed_number, "en")
print("Carrier:", carrier_name)

# Determine the timezone
time_zone = timezone.time_zones_for_number(parsed_number)
print("Time zone:", time_zone)

# Determine the location
location = geocoder.description_for_number(parsed_number, "en")
print("Location:", location)
