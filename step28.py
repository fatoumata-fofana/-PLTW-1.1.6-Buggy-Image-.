import turtle as trtl

#create turtle
painter = trtl.Turtle()
painter.pensize(40)

# Draws body
painter.circle(20)

#Setup Leg Values
legs= 8
legs_length = 100
separation = 360 / legs
painter.pensize(5)
current_leg = 0

#Draw Legs
while (current_leg < legs):
  painter.goto(0,20)
  painter.setheading(separation*current_leg)
  painter.forward(legs_length)
  current_leg = current_leg + 1
  
#Hide turtle and finish
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
