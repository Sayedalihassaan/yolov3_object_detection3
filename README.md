---

# 🧠 YOLOv3 Object Detection with OpenCV

This project demonstrates how to use the **YOLOv3 (You Only Look Once)** deep learning model for real-time object detection using OpenCV’s DNN module. It detects and classifies objects in an image using the COCO dataset.

## 📁 Project Structure

```
yolov3_object_detection/
├── yolov3_object_detection.py
├── yolov3.cfg
├── yolov3.weights
├── coco.names
└── input_image.jpg
```

## 🚀 Features

- Uses pretrained YOLOv3 weights
- Loads custom image for object detection
- Visualizes detection layers and outputs
- Color-coded bounding boxes for detected objects

## 🛠️ Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python numpy
```

## 📥 Download YOLOv3 Files

Before running the script, download these required files:

- [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
- [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

Place them in the same folder as your script or update the paths in the code accordingly.

## 🖼️ How to Run

Update the paths inside `yolov3_object_detection.py` as needed, then run:

```bash
python yolov3_object_detection.py
```

The script will:

1. Load YOLOv3 model and COCO class names.
2. Read the input image.
3. Perform object detection.
4. Print detected layers and class predictions.

## 🧠 Example Output

```
Classes
['person', 'bicycle', 'car', ...]
Number of Classes == 80
...
```

You can enhance the script by drawing bounding boxes and labels using `cv2.rectangle` and `cv2.putText`.

## 📸 Image Example

Replace the path in `cv2.imread()` with any image you'd like to test:

```python
img = cv2.imread("your_image.jpg")
```

## ✅ To Do

- [ ] Add bounding box visualization
- [ ] Support for webcam or video input
- [ ] Display confidence scores

## 📄 License

This project is licensed under the MIT License.

---
