t = 0
def setup():
    fullScreen()
    background(t)
    #frameRate (5)
def draw():
    global t
    stroke (random(0,255),random ( 0,255) , random (0,255))
    line ( random(0,width),random(0,height),   random(0,width),random(0,height))
    if t == 255:
        fill (200)
    z = random (5,50)
    ellipse ( random ( z,width-z),random ( z,height-z ) , z , z )

       
def mouseClicked():
    global t 
    if mouseButton == LEFT :
       t = color(random(0,255), random (0,255), random (0,255))
       background (t)
    if mouseButton ==  CENTER :
        saveFrame (" fotosproekta.png")
    if mouseButton == RIGHT :
       background (t)
