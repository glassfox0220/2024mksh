# -*- coding: utf-8 -*-
# 我們要在這裡把視訊鏡頭開起來
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    cv2.imshow('opencv08',img)
    # 1000ms=1s
    # 33ms=1/30s(每秒30張)
    if cv2.waitKey(33)==27:# esc=27
        break
cv2.destroyAllWindows()
    