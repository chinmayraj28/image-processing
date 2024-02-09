import cv2
import os

cropped_folder = './cropped/'
os.makedirs(cropped_folder, exist_ok=True)

x, y, w, h = 200, 50, 640, 480

p_folder = './cascade_trainer/n/'
for filename in os.listdir(p_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):  
        img_path = os.path.join(p_folder, filename)
        img = cv2.imread(img_path)

        cropped_img = img[y:y+h, x:x+w]

        cropped_path = os.path.join(cropped_folder, filename)
        cv2.imwrite(cropped_path, cropped_img)

print("Done cropping! ✅")

