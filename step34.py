# CODE TO COPY
#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# draw ladybug 
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.begin_fill()
ladybug.circle(20)
ladybug.end_fill()

# draw line on body
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)



# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)



# draw two sets of dots
while (num_dots <= 2 ): 
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1
  
# hide turtle and finish
ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()
