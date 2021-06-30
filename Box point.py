#画框，提出成片的锁定图片
import warnings
warnings.filterwarnings("ignore")
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import skimage
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.measure import label, regionprops, regionprops_table
from skimage.filters import threshold_otsu
from scipy.ndimage import median_filter
from matplotlib.patches import Rectangle
from tqdm import tqdm

def Box_point(path):
    tree = imread(path)
    tree =255-tree
    tree_blobs = label(tree > 50)
    # 展示按照区块显示的图片,展示图片的一种方式
    imshow(tree_blobs, cmap='BuGn')
    # plt.savefig("./we1_plot1.tif")
    # plt.show()

    properties = ['area', 'bbox', 'convex_area', 'bbox_area',
                  'major_axis_length', 'minor_axis_length',
                  'eccentricity']
    df = pd.DataFrame(regionprops_table(tree_blobs, properties=properties))

    blob_coordinates = [(row['bbox-0'], row['bbox-1'],
                         row['bbox-2'], row['bbox-3']) for
                        index, row in df.iterrows()]
    fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=80)
    for blob in tqdm(blob_coordinates):
        width = blob[3] - blob[1]
        height = blob[2] - blob[0]
        patch = Rectangle((blob[1], blob[0]), width, height,
                          edgecolor='r', facecolor='none')
        ax.add_patch(patch)
    ax.imshow(tree)
    ax.set_axis_off() 
    plt.savefig("WT_single_tif_for_model/Step3_boxPoint/test_box.tif")
    plt.show()
    fig, ax = plt.subplots(1, len(blob_coordinates), figsize=(15, 5))
    for n, axis in enumerate(ax.flatten()):
        axis.imshow(tree[int(blob_coordinates[n][0]):
                         int(blob_coordinates[n][2]),
                    int(blob_coordinates[n][1]):
                    int(blob_coordinates[n][3])])
    fig.tight_layout()
    plt.savefig("WT_single_tif_for_model/Step3_boxPoint/test_overlay.tif")
    plt.show()
Box_point("WT_single_tif_for_model/Step2_thin/wt1_thin.tif")