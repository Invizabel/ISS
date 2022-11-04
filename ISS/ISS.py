import re
import requests
import time
import turtle

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    result = requests.get("http://api.open-notify.org/iss-now.json").text
    result = re.findall("\d+\.\d+", result)
    iss.goto(float(result[0]), float(result[1]))
    time.sleep(15)
