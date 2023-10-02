def setup():
    global x
    global y
    size(1000, 1000)
    colorMode(HSB)
    x = 800
    y = 200
    print(x)
    print(y)
    background(0)
    

x = 0
y = 0
c = 0

xdir = 10
ydir = 10
d = 200
r = d / 2

  
def draw():
    global x
    global y
    global c

    global xdir
    global ydir
    global r
    global d

        
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 10)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
    
    noStroke()
    fill(c, 255, 255)
    circle(x, y, 200)
    x = x + xdir
    y = y + ydir
    c = c + 1
    
    if c > 255:
        c = 0
        
    if x > width - r or x < r:
        xdir = - xdir

    if y > height - r or y < r:
        ydir = - ydir
    
    # < >
    # ==
    # <=
    # >=
    # and &&
    # || or
    
    
        
