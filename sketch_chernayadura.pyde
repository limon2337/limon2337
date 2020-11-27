t = 0
def setup():
    size (400,400)
    background (0)
def draw():
    fill (t)
    z = random (5,10)
    ellipse ( random ( 0,400),random ( 0,400 ) , z , z )
    stroke ( random (1,10))
def mouseClicked():
    global t 
    if mouseButton == LEFT :
         if t == 0 :
            t = 255
         else:
            t = 0   
      
    
