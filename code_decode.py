import turtle,colorsys
screen = turtle.Screen()
screen.bgcolor("black")
hue = 0
turtle.speed(0)
for i in range(16):
    for j in range(18):
        color = colorsys.hsv_to_rgb(hue,1,1)
        hue += 0.05
        turtle.color(color)
        turtle.right(90)
        turtle.circle(150 - j*6,90)
        turtle.left(90)
        turtle.circle(150 - j*6,90)
        turtle.right(180)
    turtle.circle(40,24)
turtle.done()


   
    
