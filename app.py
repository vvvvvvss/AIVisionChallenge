from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()
model = YOLO('models/best.pt')

@app.get("/")
def home():
    return {"message": "Welcome to the AI Challenge YOLO API!"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR)
    results = model(image)
    detections = []
    for (x, y, w, h, conf, cls) in results[0].boxes.data.tolist():
        detections.append({
            'label': model.names[int(cls)],
            'confidence': float(conf),
            'bbox': [float(x), float(y), float(w), float(h)]
        })

    return {'detections': detections}
