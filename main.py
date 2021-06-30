# 入口函数
import cv2

import numpy as np
from OTSU import image_clear
from thinImage import to_binary, extract_skeleton

if __name__ == '__main__':


    # 读取图片，并显示
    image = cv2.imread("WT_single_tif_for_model\wt1.tif")
    # step1:图片初步处理，提取图片中的白色斑点，并且加深颜色
    image = image_clear(image)
    image.save("WT_single_tif_for_model/Step1_OTSU/wt1_oust.tif")
    image2 = cv2.imread("WT_single_tif_for_model/Step1_OTSU/wt1_oust.tif", 0)
    # step2:提取白色斑点的骨架，使结果更加接近overlay
    img_binary = to_binary(image2)
    # cv2.imshow("image", image2)
    # cv2.imshow("img_binary", img_binary)
    img_thin = extract_skeleton(img_binary)
    # img_thin.save("WT_single_tif_for_model/Step2_thin/wt1_oust.tif")
    cv2.imwrite("WT_single_tif_for_model/Step2_thin/wt1_thin.tif", img_thin)
    cv2.imshow("img_thin", img_thin)
    cv2.waitKey(0)
