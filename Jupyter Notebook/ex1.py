# Morphological operations

import cv2 as cv
import numpy as np

image = cv.imread("image2.jpg")

kernel = np.ones((5,5), dtype = 'uint8')
erosion = cv.erode(image, kernel, iteration = 1)
dilation = cv.dilate(image, kernel, iteration = 1)
#opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
#closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
cv.imshow("Original image ",image) #Display Original Image
cv.imshow("erosion ",erosion) #Display after erosion image
cv.imshow("dilation ",dilation) #Display after dilation image
#cv.imshow("Opening ",opening) #Display after dilation image
#cv.imshow("Closing ",closing) #Display after dilation image
cv.waitKey(0)
cv.destroyAllWindows()
