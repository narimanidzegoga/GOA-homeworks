from turtle import *


#we want to paint a house

#step 1:  draw a square

shape("turtle")

width(6)
color("midnight blue")
speed (9)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#drawing a door
forward(70)
color ("red")
left (90)
forward (100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
penup()
goto (200,200)
pendown()
color("green")
begin_fill()
right(150)
forward(200)
left (120)
forward (200)

left(120)
forward(200)

end_fill()



exitonclick()