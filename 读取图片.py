#CV中的图形特性
#读取图片
import cv2 as cv
import sys

img =cv.imread("好好学习.jpg")

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window",img)
k=cv.waitkey(0)

if k==ord("s"):
    cv.imwrite("好好学习.jpg",img)
