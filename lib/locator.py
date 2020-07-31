import requests
import time
import geoip2.database
import socket

def geo_locator(ip):

    try: 
        # check valid ip address
        socket.inet_aton(ip)     
    except:
        return None
    try:
        # in case eg database not working
        with geoip2.database.Reader("data/GeoLite2-City.mmdb") as reader:                
            response = reader.city(ip)
            country = none_checker(response.country.name)           
            area = none_checker(response.subdivisions.most_specific.name)
            city = none_checker(response.city.name)
            postal_code = none_checker(response.postal.code)
            latitude = none_checker(response.location.latitude)
            longitude = none_checker(response.location.longitude)
            
            return {"country": country, "area": area, "city":city, "postal_code": postal_code, "latitude": latitude, "longitude":longitude}          
    except: 
        return None
        
def none_checker(item):
    # checks if any values have returned None, and changes to "Unknown"
    if item == None:
        return "Unknown"
    else:
        return item   