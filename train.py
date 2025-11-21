from ultralytics import YOLO

# Load YOLOv8n pretrained
model = YOLO("yolov8n.pt")

# Train
model.train(
    data="coco128/data.yaml",
    epochs=20,
    imgsz=640,
    batch=16,
    name="yolov8_coco128"
)
