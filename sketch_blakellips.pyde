t = 0
a = 300
def setup():
    size(400,400)
    #frameRate(2)
def draw():
     background(0)
     stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
     global a
     ellipse (200,200,a,a)
     if a > 0 :
       a = a - 1
     if a == 0:
        if mousePressed:
            if a == 0: 
                a = 300
#def mouseClicked():
    #if mouseButton == LEFT :
         
        
      
    
