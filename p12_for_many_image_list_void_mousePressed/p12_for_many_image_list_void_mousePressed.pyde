
def setup():
  global imgBG,imgfox
  size(289,405)#用背景圖的大小
  imgBG=loadImage('background.jpg')
  imgfox=loadImage('foxx.jpg')#建議找半透明圖
def draw():
  global imgBG,imgfox
  image(imgBG,0,0)
  for i in range(10):
      image(imgfox,i*50,0,70,230)
  image(imgfox,mouseX,mouseY,70,230)
