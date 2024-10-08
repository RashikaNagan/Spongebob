import cv2
import numpy as np

bg = cv2.imread("Lesson 9/bg.jpg")
resize = cv2.resize(bg, (640, 480))#pass the width first instead of the height
delegate = cv2.imread("Lesson 9/spongebob.jpg")

HSV = cv2.cvtColor(delegate, cv2.COLOR_BGR2HSV)
cv2.imshow("display", HSV)


lowerrange = np.array([45,50,50]) #HSV
upperrange = np.array([80,255,255]) #HSV hue saturation value
mask = cv2.inRange(HSV, lowerrange, upperrange)

reverse = cv2.bitwise_not(mask)

combine = cv2.bitwise_and(delegate, delegate, mask = reverse )#combining
background = cv2.bitwise_and(resize, resize, mask = mask)
final = cv2.addWeighted(combine, 1, background, 0.8, 0)
cv2.imshow("display", final )


cv2.waitKey(0)