import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = jsons.load(response.read())
file = open("iss.txt","w")
file.write('They are currently ' +  str(result["number"]) + " astronauts on the iss \n\n")
people = result["people"]
for p in people :
    file.writer(p["name"] + " - on board" + "\n")

g = geocoder.ip('me')
file.writer('\n Your Current lat/ long is :' + str(g.latling))
file.close()
webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(45)
iss.penup()

input('stop')

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = jsons.loads(response.read())

    location = result["iss_position"]
    lat = location["latitude"]
    lon = location['longitude']

    lat = float(lat)
    lon = float(lon)
    print("\nlatitude:  + str(lat)")
    print("\nlongitude :" + str(lon))

    iss.goto(lon,lat)

    time.sleep(5)