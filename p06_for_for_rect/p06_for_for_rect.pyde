# p06_for_for_rect
# 在600*600裡,放10*10共100格
size(600,600)
background(255,0,0)#背景色
for x in range(10):
    for y in range(10):
        fill(255,185,239) #方塊填充
        stroke(185,253,255) #線條填充
        rect(x*60,y*60,60,60)
        
    
