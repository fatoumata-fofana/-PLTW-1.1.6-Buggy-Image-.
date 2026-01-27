import turtle as trtl

#create turtle
painter = trtl.Turtle()
painter.pensize(40)

# Draws body
painter.circle(20)

#Setup Leg Values
legs= 8
legs length = 70
separation = 380 / legs
painter.pensize(5)
current legs = 0

#Draw Legs
while (leg < legs):
  painter.goto(0,0)
  painter.setheading(separation*leg)
  painter.forward(legs length)
  leg = leg + 1
  
#Hide turtle and finish
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
