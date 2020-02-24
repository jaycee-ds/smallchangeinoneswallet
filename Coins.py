import numpy as np
import cv2

# I'm going to read the image both in grayscale and colour
image = cv2.imread('capstone_coins.png',cv2.IMREAD_GRAYSCALE)
cimage = cv2.imread('capstone_coins.png',cv2.IMREAD_COLOR)

# in order to avoid detecting false circles
image = cv2.GaussianBlur(image, (5,5), 0) 

# I'm going to detect the circles with this function and will fiddle with the parameters
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 120,param1=50,param2=27,minRadius=60,maxRadius=120)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimage,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimage,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimage)
cv2.waitKey(0)
cv2.destroyAllWindows()