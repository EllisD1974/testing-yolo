import easyocr
import cv2
import os
import time

# easyocr.utils.TQDM_BAR_FORMAT = '{l_bar}{bar}| {n_fmt}/{total_fmt}'

# reader = easyocr.Reader(['en'], gpu=False, verbose=False)
#reader = easyocr.Reader(['en'], gpu=True, verbose=False)

def get_speed_value(crop):
	gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
	result = reader.readtext(gray, detail=0)

	if len(result) > 0:
		for r in result:
			if r.isdigit():
				return r
	return None

def get_images(dir_path):
    # File extensions to consider as images
    exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    # Make everything lowercase for matching
    images = []
    for filename in os.listdir(dir_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in exts:
            images.append(os.path.join(dir_path, filename))

    return images

if __name__ == "__main__":
	print("Initializing reader")
	reader = easyocr.Reader(['en'], gpu=True, verbose=False)

	imgs_path = r"C:\developer\repos\testing-yolo\number_detection_ocr\images"
	img_paths = get_images(imgs_path)


	print("Starting classification")
	for img_path in img_paths:
		img = cv2.imread(img_path)

		speed = get_speed_value(img)
		print(f"{img_path=} {speed=}")



# speed = get_speed_value(crop)
# print("Detected speed:", speed)
