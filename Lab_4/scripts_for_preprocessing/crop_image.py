import cv2
import os
import glob

path_to_image = "./processing/frames"
path_to_frames_crop = "./processing/frames_crop"
path_to_frames_resize = "./processing/frames_resize"
images = glob.glob(os.path.join(path_to_image, "*.jpg"))
os.makedirs(path_to_frames_crop, exist_ok=True)
os.makedirs(path_to_frames_resize, exist_ok=True)
mask_coord = [
    [1300, 60],
    [835, 328],
    [660, 1050],
    [1444, 1020],
    [1670, 1077],
    [1740, 945],
    [945, 670],
    [1085, 510],
    [1600, 500],
]
start_x = 660
end_x = 1740
start_y = 0
end_y = 1080

for image_filename in images:
    image = cv2.imread(image_filename)
    image_crop = image[start_y:end_y, start_x:end_x]
    image_crop = image[start_y:end_y, start_x:end_x]
    image_resize = cv2.resize(image_crop, (512, 512))
    # image_crop = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(
        os.path.join(path_to_frames_crop, image_filename.split("/")[-1]),
        image_crop,
    )

    cv2.imwrite(
        os.path.join(path_to_frames_resize, image_filename.split("/")[-1]),
        image_resize,
    )

# new_mask_coord = [[x-start_x,y] for x,y in mask_coord]
new_mask_coord = [
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

# for x,y in new_mask_coord:
#     cv2.circle(image_crop, (x,y), 1, (255,0,0),-1)
# roi = cv2.selectROI("Roi", image)
print(new_mask_coord)
#
# cv2.imshow('Image',image_crop)
# cv2.waitKey(0)
