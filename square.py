import cv2
import glob
import os
import numpy as np

root = "normal/*"

save_dir = "icons"

files = glob.glob(root)

image_size = 20

left = True

for file in files:
	image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
	_, _, _, a = cv2.split(image)
	image = a

	suffix = file.split('/')[-1]
	
	h, w = image.shape

	if w > h:
		temp = w
		w = h 
		h = temp

	w = w - (w % 2)

	off = int((h - w) / 2)

	out = np.zeros((h, h), dtype="uint8")

	image = cv2.resize(image, (w, h))
	
	out[:, 0:off] = 0
	out[:, h-off:h] = 0
	out[:, off:h-off] = image
	out = cv2.resize(out, (image_size, image_size))
	cv2.imwrite(os.path.join(save_dir, suffix), out)
	

print("Done")