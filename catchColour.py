import cv2 as cv
import numpy as np


def separate_color(frame):
    # cv.imshow("souse", frame)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 色彩空间转换为hsv，便于分离
    lower_hsv = np.array([0, 0, 221])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])  # 提取颜色的高值
    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)  # 下面详细介绍
    # cv.imshow("inRange", mask)
    cv.imwrite("WT_single_tif_for_model/overlay/wt1_cut.tif", mask)


image = "WT_single_tif_for_model/wt1.tif"
src = cv.imread(image)
separate_color(src)

cv.waitKey(0)