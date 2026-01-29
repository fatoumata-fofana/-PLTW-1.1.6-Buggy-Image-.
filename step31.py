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
  
# RIGHT SIDE LEGS(mirror)
angle = 320
count = 0 

while count < 4:
  painter.goto(0, 20)
  painter.setheading(angle)
  painter.forward(legs_length)
  
  angle = angle + 30
  count = count + 1
  
  
# LEFT SIDE LEGS (mirror)
angle = 130
count = 0

while count < 4:
  painter.goto(0, 20)
  painter.setheading(angle)
  painter.forward(legs_length)
  
  angle = angle + 30
  count = count + 1

#Hide turtle and finish
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
