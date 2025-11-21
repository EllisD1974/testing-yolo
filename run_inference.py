from ultralytics import YOLO
import os

# Load your trained weights
model = YOLO("runs/detect/yolov8_coco128/weights/best.pt")

# Run inference on a test image
results = model("coco128/images/train/000000000009.jpg")

# Make sure the output folder exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save each result individually
for result in results:
    result.save(output_dir)  # saves annotated image and txt labels

