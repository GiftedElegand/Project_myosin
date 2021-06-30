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

def image_clear(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = gama_transfer(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 2.25)  # canny=2.25
    ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 方法选择为THRESH_OTSU
    plt.subplot(133), plt.imshow(th1, "gray")
    im = Image.fromarray(th1)
    return im


