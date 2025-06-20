from ultralytics import YOLO
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  
results = model.train(
    data='dataset.yaml',
    imgsz=640,
    epochs=50,
    batch=8,
    name='door_window_detection'
)