import re
import requests
import time
import turtle

screen = turtle.Screen()
screen.setup(1487, 840)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.title("ISS")

screen.bgpic("map.png")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

history = turtle.Pen()
history.pencolor("red")
history.width(10)
history.penup()

while True:
    try:
        result = requests.get("http://api.open-notify.org/iss-now.json").text
        result = re.findall("-\d+\.\d+|\d+\.\d+", result)
        iss.goto(float(result[0]), float(result[1]))
        history.goto(float(result[0]), float(result[1]))
        history.pendown()
        time.sleep(15)

    except:
        pass
