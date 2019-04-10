import elevation
import utm

# lat = 39.73915360
# long = -104.98470340

def convert(lat,long):

    z = elevation.getelevation(lat,long)
    (x,y) = (utm.from_latlon(lat,long)[0],utm.from_latlon(lat,long)[1])
    return x,y,z

