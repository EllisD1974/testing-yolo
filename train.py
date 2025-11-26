from ultralytics import YOLO

# Load YOLOv8n pretrained
# model = YOLO("yolov8n.pt")
model = YOLO("yolov8n_sls.pt")

# Train
# model.train(
#     data="coco128/data.yaml",
#     epochs=20,
#     imgsz=640,
#     batch=16,
#     name="yolov8_coco128"
# )

model.train(
    data="sls/data.yaml",
    epochs=20,
    imgsz=640,
    batch=16,
    name="yolov8_sls"
)
