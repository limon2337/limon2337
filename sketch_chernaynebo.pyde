t = 0
def setup():
    size (400,400)
    background (t)
def draw():
     fill (200)
     z = random (5,10)
     ellipse ( random ( 0,400),random ( 0,400 ) , z , z )
     stroke ( random (1,10))
     if mousePressed :
       background (t)
def mouseClicked():
    global t 
    if mouseButton == LEFT :
         if t == 0 :
            t =0
         else:
            t = 0 
      
    
