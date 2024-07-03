def setup():
    size(500,500)
    background(255,185,239)
def draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
        stroke(185,253,255)
        
