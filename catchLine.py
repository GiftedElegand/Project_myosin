import cv2
import numpy as np


img = cv2.imread("WT_single_tif_for_model/Step2_thin/wt1.tif",0)
cv2.imshow('origin_img', img)
height = img.shape[0]  # 高度
width = img.shape[1]  # 宽度
cut_img = img
#
# gray = cv2.cvtColor(cut_img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_img', gray)
# cv2.waitKey(0)
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(cut_img, 1, np.pi / 180, 118)
result = cut_img.copy()
minLineLength = height/32  # height/32
maxLineGap = height/40  # height/40
lines = cv2.HoughLinesP(cut_img, 1, np.pi / 180, 80, minLineLength, maxLineGap)

for x1, y1, x2, y2 in lines[0]:
    cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
