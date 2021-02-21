import cv2 as cv
import numpy as np

im = cv.imread('QRPython.png')
det = cv.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = det.detectAndDecodeMulti(np.hstack([im, im]))
print(straight_qrcode)