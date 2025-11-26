import pytesseract
import cv2
from PIL import Image

# If Tesseract is not in PATH, set it manually:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def get_speed_value(crop):
    # Preprocess to improve OCR accuracy
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)[1]

    pil_img = Image.fromarray(thresh)

    text = pytesseract.image_to_string(
        pil_img,
        config="--psm 8 -c tessedit_char_whitelist=0123456789"
    )

    return text.strip()

if __name__ == "__main__":
	img_path = r"C:\developer\repos\testing-yolo\number_detection_ocr\images\cropped_speed_sign_25_mph.png"
	img = cv2.imread(img_path)
	
	speed = get_speed_value(img)
	print(f"{speed=}")

# Example usage:
# speed = get_speed_value(crop)
# print("Detected speed:", speed)
