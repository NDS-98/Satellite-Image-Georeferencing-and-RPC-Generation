import json
import urllib.request

def getelevation(lat,long):
    response = urllib.request.urlopen("https://maps.googleapis.com/maps/api/elevation/json?locations=" + str(lat) + "," + str(long) + "&key=AIzaSyDTJkkx8M1hzY3OpG-lL66LmoBYoZRKMBg")
    return float(json.load(response)["results"][0]["elevation"])
















































































