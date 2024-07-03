#p13_for_list_append
def setup():
  global imgBG,imgfox
  size(289,405)#用背景圖的大小
  imgBG=loadImage('background.jpg')
  imgfox=loadImage('dot.png')#建議找半透明圖
def draw():
  global imgBG,imgfox
  image(imgBG,0,0)
  for i in range(len(x)):
      image(imgfox,x[i],y[i],10,10)
      
  image(imgfox,mouseX,mouseY,10,10)
x=[]#x=[0]*10
y=[]#y=[0]*10
#N=0
def mousePressed():#滑鼠點下時做事情
    x.append(mouseX)#global N
    y.append(mouseY)#x[N],y[N]= mouseX,mouseY
    #N+=1#N慢慢增加
