
a=[
   [1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1],
   [2,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2],
   [2,2,1,1,1,2,2,2,2,1,1,1,1,2,2,2],
   [2,2,2,1,1,1,2,2,2,2,1,1,1,1,2,2]]

size(480,480)
for x in range(len(a)):
    for y in range(16):
        
        if(x+y)%2==1:
            fill(0)#白色
        else:
            fill(255)#黑色
            
        rect(y*30,x*30,30,30)
        
        if(x+y)%2==1:
            fill(255)#黑色
        else:
            fill(0)#白色
            
        if a[x][y]==1:
            rect(y*30+2,x*30+2,9,9)
            rect(y*30+19,x*30+19,9,9)
        else:
            rect(y*30+19,x*30+2,9,9)
            rect(y*30+2,x*30+19,9,9)
