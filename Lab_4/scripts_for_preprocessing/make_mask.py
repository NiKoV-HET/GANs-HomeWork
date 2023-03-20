import cv2
import numpy
import os
import glob

import numpy as np

path_to_image = "./processing/frames_crop"
path_to_mask = "./processing/mask"
os.makedirs(path_to_mask, exist_ok=True)
images = glob.glob(os.path.join(path_to_image, "*.jpg"))
mask_coord = np.array(
    [
        [640, 60],
        [175, 328],
        [0, 1050],
        [784, 1020],
        [1010, 1077],
        [1080, 945],
        [285, 670],
        [425, 510],
        [940, 500],
    ]
)
for image_filename in images:
    image = cv2.imread(image_filename)
    h, w, c = image.shape
    mask = np.full((h, w), 255, dtype="uint8")
    cv2.fillPoly(mask, [mask_coord], (0, 0, 0))
    mask = cv2.resize(mask, (512, 512))
    cv2.imwrite(
        os.path.join(path_to_mask, image_filename.split("/")[-1]),
        mask,
    )
