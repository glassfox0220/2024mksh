
size(480,480)
for x in range(16):
    for y in range(16):
        if(x+y)%2==1:
            fill(255)#白色
        else:
            fill(0)#黑色
            
        rect(x*30,y*30,30,30)
        
        if(x+y)%2==1:
            fill(0)#黑色
        else:
            fill(255)#白色
            
        rect(x*30+2,y*30+2,9,9)
        rect(x*30+19,y*30+19,9,9)
