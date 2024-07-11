# -*- coding: utf-8 -*-
import cv2
# 要先把圖檔放在同一個目錄(桌面)
# 小心副檔名 檔案總管-檢視-(勾)副檔名
img=cv2.imread('fox.jpg')
b=img[:,:,0]
print(b)
cv2.imshow('opencv06',img)
cv2.waitKey(3000)# 等按空白鍵
# 等3秒鐘,都沒按鍵,就離開
cv2.destroyAllWindows()# 關閉視窗