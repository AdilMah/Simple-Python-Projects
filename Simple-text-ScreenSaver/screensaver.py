##This simple GUI Python program prints a text on the screen and its position changes continuosly

import simplegui
import random
#Global variables initialised
message="Adil Mahmood"
width=400
height=200
position=[100,100]
interval=2000

#Helper functions
def update(text):
    global message
    message=text
    
def tick():
    newwidth=random.randrange(0,width)
    newheight=random.randrange(0,height)
    position[0]=newwidth
    position[1]=newheight
def draw(canvas):
    canvas.draw_text(message,position,36,"red")
    
#Created a frame using simplegui
frame=simplegui.create_frame("screen",width,height)

#Initialised all the event handlers
text=frame.add_input("Message:::",update,150)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(interval,tick)

frame.start()
timer.start()

  
