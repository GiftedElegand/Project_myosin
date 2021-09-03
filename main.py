
import cv2

import numpy as np
from OTSU import image_clear
from thinImage import to_binary, extract_skeleton

if __name__ == '__main__':
    path_original = "WT_single_tif_for_model/"
    path_step1 = "WT_single_tif_for_model/Step1_OTSU/"
    path_step2 = "WT_single_tif_for_model/Step2_thin/"
    path_step3 = "WT_single_tif_for_model/Step3_boxPoint/"
    # image name
    name = "wt22"
    image_type = ".tif"
    # Read the picture
    image = cv2.imread(path_original+name+image_type)

    # step1:The image is preliminarily processed, the white spots in the image are extracted, and the color is deepened
    image = image_clear(image)
    image.save(path_step1+name+image_type)


    # step2:Extract the skeleton of the white spots to make the result closer to overlay
    image2 = cv2.imread(path_step1 + name + image_type, 0)
    # image2 = cv2.imread("WT_single_tif_for_model/wt1.tif", 0)


    img_binary = to_binary(image2)

    cv2.imshow("image", image2)
    cv2.imshow("img_binary", img_binary)
    img_thin = extract_skeleton(img_binary)
    # img_thin.save("WT_single_tif_for_model/Step2_thin/wt1_oust.tif")
    cv2.imwrite(path_step2+name+image_type, img_thin)
    cv2.imshow("img_thin", img_thin)
    cv2.waitKey(0)

