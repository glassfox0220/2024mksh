# -*- coding: utf-8 -*-
import cv2

img=cv2.imread('foxx.jpg')
b=img[:,:,0]#   冒號,冒號,0 藍色
g=img[:,:,1]#   冒號,冒號,1 綠色
r=img[:,:,2]#   冒號,冒號,2 紅色

img_rbb=cv2.merge([r,b,b])
cv2.imwrite('rbb.png',img_rbb)# (檔名,檔案)
cv2.imshow('RBB',img_rbb)
cv2.imshow('opencv02',img)

cv2.waitKey(0)# K大寫
# 如果按下任意鍵,會把全部的視窗都關閉
cv2.destroyAllWindows()