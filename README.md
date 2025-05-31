# AI Vision Exercise: Door and Window Detection in Blueprints

This project implements an AI model to detect doors and windows in architectural blueprints. It involves manual labeling, training a YOLOv8 model, and deploying a FastAPI endpoint for inference.

## Project Structure

## Overview
An AI-powered API that detects doors and windows in architectural blueprints using YOLOv8.

## Classes
- `door`: Detects door symbols in blueprints
- `window`: Detects window symbols in blueprints

## Setup Instructions

1. Install dependencies:

`pip install ultralytics fastapi python-multipart uvicorn opencv-python numpy`



## Classes Used

The model is trained to detect the following two classes:

1.  `door`
2.  `window`

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    # git clone <your-repo-url>
    # cd <your-repo-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: `requirements.txt` should include `fastapi`, `uvicorn`, `ultralytics`, `python-multipart`, `opencv-python`, etc.*

4.  **Download images:**
    Ensure the blueprint images are placed in the `images/` directory. You can download them from [here](https://drive.google.com/drive/folders/1Uj_Lop-g9uNFzrXFHoT5xt8zgaFKJWgP?usp=sharing).

5.  **Prepare Labels:**
    *   Use LabelImg (included in the `labelImg/` directory or install separately) to annotate images in the `images/` folder.
    *   Save annotations in YOLO format (`.txt` files) into the `labels/` directory.
    *   Ensure `classes.txt` at the project root contains `door` and `window` on separate lines.
    *   Run the provided script or manually split your `images/` and `labels/` data into `dataset/train/images`, `dataset/train/labels`, `dataset/val/images`, and `dataset/val/labels` (e.g., 80% train, 20% val).  
![image](https://github.com/user-attachments/assets/4ceef6b2-d004-41e0-9dfa-9c6ff9e57373)  

6.  **Train the model (if `models/best.pt` is not provided or you want to retrain):
    ```bash
    python train.py
    ```
    This will use `dataset.yaml` for configuration and save the best model to `runs/detect/<experiment_name>/weights/best.pt`. Copy this to `models/best.pt` for the API to use.
    ![image](https://github.com/user-attachments/assets/758c99af-53db-4690-9835-dae090480b53)  

![image](https://github.com/user-attachments/assets/da1ce388-25fa-4117-9563-325221285298)  

## Running the API

1.  **Start the FastAPI server:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 10000
    ```
    https://blueprint-door-window-detection.onrender.com

## API Usage

### `POST /detect`

This endpoint accepts a `PNG` or `JPG` blueprint image and returns detected objects (doors and windows) with their bounding boxes, labels, and confidence scores.

**Request:** `multipart/form-data` with a file field named `file`.

**`curl` Example:**

```bash
curl -X POST -F "file=@/path/to/your/image.png" http://localhost:10000/detect
