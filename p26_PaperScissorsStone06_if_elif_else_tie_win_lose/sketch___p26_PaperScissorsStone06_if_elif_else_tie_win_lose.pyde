# p26_PaperScissorsStone06_if_elif_else_tie_win_lose
import random
select,PC=-1,-1
def setup():
    size(600,300)
def draw():
    fill(255)#白色的格子
    rect(0,0,300,300)
    rect(300,0,300,300)
    for i in range(3):
        if PC==i:fill(255,0,0)
        else:fill(255)
        rect(100,100+i*50,100,50)
    for i in range(3):
        if select==i:fill(255,0,0)
        else:fill(255)
        rect(400,100+i*50,100,50)
    textSize(25)#文字大小
    textAlign(LEFT,TOP)#文字對齊左上
    fill(0)#黑字
    for i in range(2):
        text("Paper",100+i*300,100)
        text("Scissor",100+i*300,150)
        text("Stone",100+i*300,200)
def mousePressed():#如果mouse按下去
    global select,PC
    select=-1#沒有任何選擇
    if 400<mouseX<400+100:#左右在範圍內
        if 100<mouseY<150:select=0#在上下範圍內
        if 150<mouseY<200:select=1
        if 200<mouseY<250:select=2 
        PC=int(random.randrange(3))
    if select<=2 and select>=0:
        if (PC==0 and select==2) or \
        (PC==1 and select==0) or \
        (PC==2 and select==1):
            print('lose')
        elif PC==select:
            print("tie")
        else:
            print('win)

        
            
