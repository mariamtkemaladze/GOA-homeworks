from turtle import*

speed(30)
width(7)

color("gray")

begin_fill()
forward(100)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(100)
end_fill()

penup()
goto(100,0)
pendown()
begin_fill()
forward(150)
left(90)
forward(100)
left(90)
forward(150)
end_fill()

penup()
goto(-100, 0)
pendown()
begin_fill()
forward(150)
right(90)
forward(100)
right(90)
forward(150)
end_fill()

color("red")
begin_fill()
left(130)
forward(120)
left(102)
forward(119)
end_fill()


penup()
goto(100, 200)
pendown()
begin_fill()
right(100)
forward(150)
left(96)
forward(150)
end_fill()

penup()
goto(250, 100)
pendown()
begin_fill()
right(90)
forward(100)
left(86)
forward(98)
end_fill()

penup()
goto(-300, -5)
color("green")
pendown()
right(224)
forward(600)
right(90)
forward(3)
right(90)
forward(600)

right(180)
forward(200)
left(90)
forward(5)
color("black")
forward(205)
right(90)
forward(200)
right(90)
forward(200)
left(90)
forward(150)
left(90)
forward(100)
left(90)
forward(150)

penup()
goto(-100, 0)
pendown()
forward(150)
right(90)
forward(100)
right(90)
forward(150)
penup()
goto(-100, 0)
pendown()
forward(205)

#finished

exitonclick()