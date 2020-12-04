t = 0
def setup():
    size (400,400)
    background(t)
def draw():
    global t
    stroke (random(0,255),random ( 0,255) , random (0,255))
    line ( random(0,400),random(0,400),random(0,400),random(0,400))
    if t == 255:
        fill (200)
    z = random (5,10)
    ellipse ( random ( 0,400),random ( 0,400 ) , z , z )
    stroke ( random (1,10))

       
def mouseClicked():
    global t 
    if mouseButton == LEFT :
       t = color(random(0,255), random (0,255), random (0,255))
       background (t)
    if mouseButton ==  CENTER :
        saveFrame (" fotosproekta.png")
    if mouseButton == RIGHT :
       background (t)
