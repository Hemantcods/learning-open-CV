import cv2 as cv
import numpy as np

img=cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

# blank img
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

# mask
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

# masked img
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)


cv.waitKey(0)