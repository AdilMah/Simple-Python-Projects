import simplegui
import math
width=1366
length=768
ball_list=[]
ball_radius=15

def distance(p,q):
      return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    

        
def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0],ball[1]],ball_radius,1,"Black","Red")
                       


frame=simplegui.create_frame("Ball Game",width,length)
frame.set_canvas_background("White")

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()
