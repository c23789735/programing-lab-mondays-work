def setup():
    size (500,500)
    colorMode(HSB)
    noStroke()
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global rad
    rad=10
    x1=height/2
    y1=width/2
    x2=height/2
    y2=width/2
    x3=height/2
    y3=width/2
    x4=height/2
    y4=width/2
    background(0)
    
    
def draw():
    global rad
    global x1
    global y1
    fill(x1,255,255)
    circle(x1,y1,rad)
    x1-=1
    y1-=1
    global x2
    global y2
    fill(x1,255,255)
    circle(x2,y2,rad)
    x2-=1
    y2+=1
    global x3
    global y3
    fill(x1,255,255)
    circle(x3,y3,rad)
    x3+=1
    y3-=1
    global x4
    global y4
    fill(x1,255,255)
    circle(x4,y4,rad)
    x4+=1
    y4+=1
    if x1<100:
        rad +=1
        
    else:
        rad -=1
    

    
