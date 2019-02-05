import numpy as np
import cv2
imgFile = cv2.imread('messi.jpeg')

cv2.imshow('dst_rt', imgFile)
cv2.waitKey(0)
cv2.destroyAllWindows()
