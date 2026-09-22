import os
import sys
import cv2
import json
from ultralytics import YOLO

def apply_speckle_filter(img):
    # The same edge-preserving radar filter you built in Phase 2
    return cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

def run_production_pipeline(image_path, weights_path="best.pt"):
    if not os.path.exists(image_path):
        print(json.dumps({"error": f"Input image {image_path} not found"}))
        return

    # 1. Load image in grayscale (SAR standard)
    raw_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Preprocess: Clean radar noise
    cleaned_img = apply_speckle_filter(raw_img)
    
    # Save a temporary clean image for YOLO to read
    temp_path = "temp_processed.png"
    cv2.imwrite(temp_path, cleaned_img)

    # 3. Load Model and Predict (Forcing CPU for universal cloud compatibility)
    model = YOLO(weights_path)
    results = model.predict(source=temp_path, conf=0.25, verbose=False)
    
    # 4. Extract structured JSON telemetry data 
    output_predictions = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            coords = box.xyxy[0].tolist() # [xmin, ymin, xmax, ymax]
            conf = float(box.conf[0])
            output_predictions.append({
                "class": "ship",
                "confidence": round(conf, 4),
                "bounding_box": [round(c, 2) for c in coords]
            })

    # Clean up temp file
    if os.path.exists(temp_path):
        os.remove(temp_path)

    # Print clean JSON output to standard output stream
    print(json.dumps({"status": "success", "detections": output_predictions}, indent=2))

if __name__ == "__main__":
    # Allows image path injection via command line arguments
    img_arg = sys.argv[1] if len(sys.argv) > 1 else "test_target.png"
    run_production_pipeline(img_arg)
