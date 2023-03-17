import phonenumbers
from phonenumbers import geocoder 
phone_number1 = phonenumbers.parse("+351000000000")

print("\nPhone Numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"))

