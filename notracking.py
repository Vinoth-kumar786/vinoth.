import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier 
from phonenumbers import timezone
number =input("Enter number:")
print()
ch_number=phonenumbers.parse(number,"CH")
number_country=geocoder.description_for_number(ch_number,"en")\

service_provider= phonenumbers.parse(number,"RO")
number_provider= carrier.name_for_number(service_provider,"en")

phone_number= phonenumbers.parse(number)
time_zone= timezone.time_zones_for_number(phone_number)

print("\n country:",number_country)
print("\n TimeZone and region:",time_zone)
print("\n service/carrier provider:",number_provider)
print()