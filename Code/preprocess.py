import cv2
import numpy as np

img = cv2.imread("Data/detect_blob.png")
print(img.shape)
img_resize = cv2.resize(img, (200,200) ) #x,y

imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hz = np.hstack((img, imgHsv))
cv2.imshow("hsv",hz)
cv2.waitKey(5000)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thres_adapt = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115, 1)
hz = np.hstack((imgGray, thres_adapt))
cv2.imshow("hsv",hz)
cv2.waitKey(5000)

