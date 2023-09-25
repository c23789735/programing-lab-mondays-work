def setup():
    global x
    global y
    global w
    global hw
    global xdir
    size (500 , 500)
    colorMode(HSB)
    noStroke()
    y=height/2
    w=50
    hw=w/2
    x=hw
    xdir=1
    
def draw():
    background(0)
    global x
    global xdir
    fill(x/2,255,255)
    circle(x,y,w)
    x+=xdir
    if x==width+hw:
        xdir-=1
        
