import os
import cv2

path_to_video = "./masked_video.mp4"
path_to_save = "./processing/frames"
os.makedirs(path_to_save, exist_ok=True)

cap = cv2.VideoCapture(path_to_video)
ret = True
count = 0
while ret:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(path_to_save, f"{count}.jpg"), frame)
        count += 1
