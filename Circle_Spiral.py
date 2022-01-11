
import turtle as tur
 

tur.bgcolor('black')
tur.pensize(2)
tur.speed(10**3)

radius = 40

color_range = ('green', 'yellow', 'red','pink', 'blue', 'orange','cyan')* 5

for i in range(3):

      
    for color in color_range:
        tur.color(color)
        tur.circle(radius)
        tur.left(10)
    
    radius += 20

tur.hideturtle()
