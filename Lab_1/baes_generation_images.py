import cv2
import glob
import os
import numpy as np

# Read Images
img_path = 'avatars'
images = glob.glob(os.path.join(img_path,'*png'))

# Get params
h, w, c = cv2.imread(images[0]).shape
resizeH = h
resizeW = None
pix = {}

# Get all pixels
for image in images:
    image_cv = cv2.imread(image)
    h, w, c = cv2.imread(images[0]).shape
    coef = h/w

    resizeW = int(resizeH/coef)
    image_cv = cv2.resize(image_cv, (resizeH, resizeW))

    for i in range(resizeW):
        for j in range(resizeH):
            for k in range(c):
                if f"{i},{j},{k}" in pix:
                    pix[f"{i},{j},{k}"].append(image_cv[i][j][k])
                else:
                    pix[f"{i},{j},{k}"] = [image_cv[i][j][k]]

# Create array for new image
new_img = [[[255 for _ in range(c)]for _ in range(resizeW)] for _ in range(resizeH)]

# Get new image
for k,v in pix.items():
    w,h,c = map(int,k.split(","))
    new_img[h][w][c] = np.random.choice(v)  # I keep all the pixels and so the normal selection can be used

# List to np.array and transpose
new_img = np.array(new_img, dtype="uint8").transpose((1,0,2))

# Save image
cv2.imwrite("new_image.jpg", new_img)
# cv2.imshow("new_image", new_img)
# cv2.waitKey(1)
print("New image was created!")
