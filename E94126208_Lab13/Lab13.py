import cv2
import numpy as np
image = cv2.imread("/Users/jimshih/Downloads/TW.jpg") 
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
B,G,R = cv2.split(image) #split BGR channel
gray2 = (B+G+R)/3 
#output = cv2.THRESH_BINARY(image,127,255,cv2.THRESH_BINARY)
#print(B)
#print(gray2)
#print(gray)
zeros = np.zeros(image.shape[:2],dtype="uint8") # create與image一樣大小的0矩陣
cv2.imshow("Sun", image) #原圖
cv2.imshow("gray", img_gray)#使用函式
cv2.imshow("gray2", gray2.astype(np.uint8))#未使用函式
ret,output = cv2.threshold(img_gray,245,255,cv2.THRESH_BINARY)
cv2.imshow("gray3", output) #二值化



cv2.waitKey(0)
cv2.destroyAllWindows()