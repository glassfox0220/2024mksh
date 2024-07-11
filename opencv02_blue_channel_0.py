# -*- coding: utf-8 -*-

import cv2# 使用OpenCV的cv2外掛
#   匯入cv2
img=cv2.imread('foxx.jpg')
#   讀入opencv.png 這張圖
cv2.imshow('one',img)#  要在'one'秀圖
cv2.imshow('hello',img)#  要在'one'秀圖
cv2.imshow('mksh',img)#  要在'one'秀圖
cv2.waitKey(0)# 等待任意鍵,卡住,不要結束
#   File-New Ctrl-N 開新檔案
#   File-Save as 令存新檔 opencv01.py
#   存在桌面的 opencv01.py
#   Win+E檔案總管
#   沒有圖，不要執行，會當掉