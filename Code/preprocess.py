import cv2
import numpy as np
import matplotlib.pyplot as plt

file_paths = ['../Data/train/vacant','../Data/train/occupied']
classes=[0,1]
for c in classes:
    for i in range(9):
        plt.subplot(330 +i +1)
        filename = file_paths[c] + f"/{c} ({i}).jpg"
        img=cv2.imread(filename)
        img_resize = cv2.resize(img, (900, 400))  # x,y
        color = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
        imgGray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
        imgCanny = cv2.Canny(imgBlur, 120, 120)  # edge detection

        plt.imshow(imgCanny, cmap=plt.cm.gray)
    plt.show()