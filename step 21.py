
# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
# Draws body
painter.circle(20)
#Draws Legs
legs= 8
legs length = 70
separation = 380 / legs
painter.pensize(5)
current legs = 0
while (leg < legs):
  painter.goto(0,0)
  painter.setheading(separation*leg)
  painter.forward(legs length)
  leg = leg + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
