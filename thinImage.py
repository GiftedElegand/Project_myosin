import cv2
import copy


# 映射表
l_array = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
           1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
           0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
           1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
           1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
           0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
           1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
           1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]


def v_thin(img):
    """
    细化函数，根据算法，运算出中心点的对应值
    :param img: 需要细化的图片（经过二值化处理的图片）
    :param array: 映射矩阵array
    :return:
    """
    h, w = img.shape
    i_next = 1
    for i in range(h):
        for j in range(w):
            if i_next == 0:
                i_next = 1
            else:
                i_m = int(img[i, j - 1]) + int(img[i, j]) + int(img[i, j + 1]) if 0 < j < w - 1 else 1
                if img[i, j] == 0 and i_m != 0:
                    a = [0] * 9
                    for k in range(3):
                        for l in range(3):
                            if -1 < (i - 1 + k) < h and -1 < (j - 1 + l) < w and img[i - 1 + k, j - 1 + l] == 255:
                                a[k * 3 + l] = 1
                    i_sum = a[0] * 1 + a[1] * 2 + a[2] * 4 + a[3] * 8 + a[5] * 16 + a[6] * 32 + a[7] * 64 + a[8] * 128
                    img[i, j] = l_array[i_sum] * 255
                    if l_array[i_sum] == 1:
                        i_next = 0


def h_thin(img):
    """
    细化函数，根据算法，运算出中心点的对应值
    :param img: 需要细化的图片（经过二值化处理的图片）
    :param array: 映射矩阵array
    :return:
    """
    h, w = img.shape
    i_next = 1
    for j in range(w):
        for i in range(h):
            if i_next == 0:
                i_next = 1
            else:
                i_m = int(img[i -1, j]) + int(img[i, j]) + int(img[i + 1, j]) if 0 < i < h - 1 else 1
                if img[i, j] == 0 and i_m != 0:
                    a = [0] * 9
                    for k in range(3):
                        for l in range(3):
                            if -1 < (i - 1 + k) < h and -1 < (j - 1 + l) < w and img[i - 1 + k, j - 1 + l] == 255:
                                a[k * 3 + l] = 1
                    i_sum = a[0] * 1 + a[1] * 2 + a[2] * 4 + a[3] * 8 + a[5] * 16 + a[6] * 32 + a[7] * 64 + a[8] * 128
                    img[i, j] = l_array[i_sum] * 255
                    if l_array[i_sum] == 1:
                        i_next = 0


def extract_skeleton(img, num=10):
    for i in range(num):
        v_thin(img)
        h_thin(img)

    return img


def to_binary(img):
    """
    二值化函数，阈值根据图片的昏暗程序自己设定
    :param img: 需要二值化的图片
    :return:
    """
    w, h = img.shape
    i_two = copy.deepcopy(img)
    for i in range(w):
        for j in range(h):
            if img[i, j] < 200:
                i_two[i, j] = 255
            else:
                i_two[i, j] = 0

    return i_two
