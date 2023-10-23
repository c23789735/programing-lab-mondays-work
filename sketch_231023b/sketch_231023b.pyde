def setup():
    global cx, cy
    global px, py
    size(500, 500)
    # fullScreen()
    colorMode(HSB)
    cx = width / 2
    cy = height /2
    px = cx
    py = cy
    
cx = 0
cy = 0
r = 150
angle = 0
angle2 = 0

px = 0
py = 0
    
def draw():    
    global cx, cy
    global px, py
    num = 3
    num2 = 15
    theta = TWO_PI / num
    theta2 = TWO_PI / num2
    
    background(0)
    translate(cx, cy)
    
        
    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        fill(255)
        stroke(200)
        ellipse(0, 100, 150, 200)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        fill(255)
        stroke(200)
        ellipse(100, 0, 200, 150)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        fill(255)
        stroke(200)
        ellipse(-100, 0, 200, 150)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        fill(255)
        stroke(200)
        ellipse(0, -100, 150, 200)
        #line(0, 0, 0, 100)            
        popMatrix()
        
        
        
    for i in range(num2):
        angle2 = theta2 * i
        pushMatrix()
        rotate(angle2)
        stroke(30,200,200)
        fill(30,255,255)
        ellipse(0, 55, 5, 75)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num2):
        angle2 = theta2 * i
        pushMatrix()
        rotate(angle2)
        stroke(30,200,200)
        fill(30,255,255)
        ellipse(55, 0, 75, 5)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num2):
        angle2 = theta2 * i
        pushMatrix()
        rotate(angle2)
        stroke(30,200,200)
        fill(30,255,255)
        ellipse(0, -55, 5, 75)
        #line(0, 0, 0, 100)            
        popMatrix()
        
    for i in range(num2):
        angle2 = theta2 * i
        pushMatrix()
        rotate(angle2)
        stroke(30,200,200)
        fill(30,255,255)
        ellipse(-55, 0, 75, 5)
        #line(0, 0, 0, 100)            
        popMatrix()
        
        
    fill(255)
    stroke(200)
    ellipse(0, 0, 65, 65)
    stroke(40,200,200)
    fill(40,255,255)
    ellipse(0,0,60,60)        
