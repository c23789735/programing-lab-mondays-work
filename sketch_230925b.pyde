def setup():
    colorMode (HSB) # colorMode (RGB)
    size (1000, 1000)
    
def draw():
    # Greyscale
    
    f=10.0 # variable in global scope
    g=20.0
    h=5
    
    f=f+1
    f+=1#12
    
    g-=30
    g=g-27#-37
    
    g=f*h#60
    h*=2#10
    
    g=f/h#1.2
    h=h/2.5#4
    
    f=pow(g,2)#1.44
    h= h-7#-3
    g+=f#2.64
    f+=g#4.08
    h=f-(g+5)#-3.56
    
    println(f)
    println(g)
    println(h)
    
    println(f/2)
    println(f)
    
    # RGB
    # RGBA
    background(0,255,255)
    stroke(90,255,255)
    point(90,100)
    line (mouseX,10,100,mouseY)
    rect (20,20,50,100) # rectMode(CENTER) rectMode(CORNERS)
    circle(100,mouseY,5)
    fill(90,mouseX / 2,255)
    ellipse(200,200,100,10)
