def setup():
    size (400,400)
def draw():
    if mousePressed:
        strokeWeight (10)
        line ( mouseX,mouseY, pmouseX,pmouseY )
    if keyPressed:
        if key == "1":
            stroke (255,0,0)
        if key == "2":
            stroke (0,255,0)
        if key == "3":
            stroke (0,0,255)
        if key == "4":
            stroke (255,255,0)
        if key == "5":
            stroke (255,0,255)
        if key == "6":
            stroke (255,255,255)
        if key == "7":
            stroke (0,0,0)
        if key == " ":
             background(100)
        if key == CODED:
             CODED=
              
            
