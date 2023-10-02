def setup():
    size (500,500)
    colorMode(HSB)
    
def draw():
    background(200,200,255)
    noStroke()
    fill(20,225,255)
    if mouseX<width/2 and mouseY<height/2:
        rect (0,0,width/2,height/2)
    else:
        rect(width/2,0,width/2,height/2)
    if mouseX>width/2 and mouseY>height/2:
        rect (0,height/2,width/2,height/2)
    else:
        rect(width/2,height/2,width/2,height/2)
    fill(0,255,255)
    if mouseX>width/2 and mouseY<height/2:
        rect (0,height/2,width/2,height/2)
    else:
        rect(width/2,height/2,width/2,height/2)
    fill(100,255,255)    
    if mouseX<width/2 and mouseY>height/2:
        rect (0,height/2,width/2,height/2)
    else:
        rect(width/2,height/2,width/2,height/2)
        
