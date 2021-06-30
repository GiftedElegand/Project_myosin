#coding:utf-8
import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def gama_transfer(img,power1):
    if len(img.shape) == 3:
         img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = 255*np.power(img/255,power1)
    img = np.around(img)
    img[img>255] = 255
    out_img = img.astype(np.uint8)
    return out_img

image = cv2.imread("I:\Jupyter\pythonProject\ProjectGG\WT_single_tif_for_model\wt1.tif")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = gama_transfer(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),2.25)
tmpgray = gray

plt.subplot(131), plt.imshow(tmpgray, "gray")
plt.title("source image"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.hist(image.ravel(), 256)
plt.title("Histogram"), plt.xticks([]), plt.yticks([])
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU
plt.subplot(133), plt.imshow(th1, "gray")
plt.title("OTSU,threshold is " + str(ret1)), plt.xticks([]), plt.yticks([])
im = Image.fromarray(th1)
im.save("I:\Jupyter\pythonProject\ProjectGG\WT_single_tif_for_model\we1.tif")
plt.show()
