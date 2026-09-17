import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = "+919876543210"
number_country = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(number_country, "en"))

service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

time_zone = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(time_zone))
