import cv2 as cv
import numpy as np
#边缘分割

def edge(img):
    #高斯模糊,降低噪声
    blurred = cv.GaussianBlur(img,(3,3),0)
    #灰度图像
    gray=cv.cvtColor(blurred,cv.COLOR_RGB2GRAY)
    #图像梯度
    xgrad=cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad=cv.Sobel(gray,cv.CV_16SC1,0,1)
    #计算边缘
    #50和150参数必须符合1：3或者1：2
    edge_output=cv.Canny(xgrad,ygrad,50,150)
    #图一
    cv.imshow("edge",edge_output)
    # img2.save("I:\Jupyter\pythonProject\ProjectGG\WT_single_tif_for_model\we1_adge.tif")
    dst=cv.bitwise_and(img,img,mask=edge_output)
    #图二（彩色）
    cv.imshow('cedge',dst)

def gama_transfer(img,power1):
    if len(img.shape) == 3:
         img= cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img = 255*np.power(img/255,power1)
    img = np.around(img)
    img[img>255] = 255
    out_img = img.astype(np.uint8)
    return out_img

#线性锐化
image = cv.imread("I:\Jupyter\pythonProject\ProjectGG\WT_single_tif_for_model\wt2.tif")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = gama_transfer(cv.cvtColor(image, cv.COLOR_BGR2GRAY), 2.25)
tmpgray = gray


src = cv.imread('I:\Jupyter\pythonProject\ProjectGG\WT_single_tif_for_model\wt1.tif')
#图三（原图）
cv.imshow('def',src)
edge(src)

cv.waitKey(0)
cv.destroyAllWindows()