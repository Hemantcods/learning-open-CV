# contours mean boundary on objects
import cv2 as cv
import numpy as np



img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

# blank
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)


# canny=cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)

# thresholding
ret,threshold=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold',threshold)





contours,hierachies=cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')


# drawing contours to the blaank

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)




cv.waitKey(0)