import simplegui
import math
width=1366
length=768
ball_list=[]
ball_radius=15

def distance(p,q):
      return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    

        
def click(pos):
    changed=False
    for ball in ball_list:
        if distance([ball[0],ball[1]],pos)<ball_radius:
            changed=True
            ball[2]="Green"
    if not changed:
            ball_list.append([pos[0],pos[1],"Red"])

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0],ball[1]],ball_radius,1,"Black",ball[2])
                       


frame=simplegui.create_frame("Ball Game",width,length)
frame.set_canvas_background("White")

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()
