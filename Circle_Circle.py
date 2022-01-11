import turtle as tur

tur.bgcolor('black')
tur.pensize(2)
tur.speed(10**10)


color_range = ('green', 'yellow', 'red','pink', 'blue', 'orange','cyan')* 2
ptr = 0
  
for i in range(10, 250, 5):

    tur.color(color_range[ptr])
    tur.circle(i)
    ptr = (ptr + 1) % len(color_range)
    tur.left(2)

for i in range(250, 10, -5):

    tur.color(color_range[ptr])
    tur.circle(i)
    ptr = (ptr + 1) % len(color_range)
    tur.left(2)

for i in range(10, 250, 5):

    tur.color(color_range[ptr])
    tur.circle(i)
    ptr = (ptr + 1) % len(color_range)
    tur.left(2)

for i in range(250, 10, -5):

    tur.color(color_range[ptr])
    tur.circle(i)
    ptr = (ptr + 1) % len(color_range)
    tur.left(2)
