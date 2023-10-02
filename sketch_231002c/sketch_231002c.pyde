def setup():
    size(500,500)
    noStroke()
    colorMode(HSB)
    
def draw():
    background(200,200,200)
    fill(20,200,200)
    if mouseX<200 or mouseY<200  or mouseX>300 or mouseY>300:
        rect(200,200,100,100)
    else:
        fill(150,200,200)
        rect(200,200,100,100)
