def setup():
    size(300,300)
def draw():
    background(255)
    for x in range(0,300,20):
        for y in range(0,300,20):
            noFill()
            ellipse(x,y,40,40)
            fill(0)
            r=4
            a=frameCount*PI/360
            ellipse(x+r*cos(a),y+r*sin(a),5,5)
       
            
        
