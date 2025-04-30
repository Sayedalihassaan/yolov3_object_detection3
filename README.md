
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
- Ready for bounding box visualization with confidence scores

## 🛠️ Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies using:

```bash
pip install opencv-python numpy
```

## 📥 Download YOLOv3 Files

Before running the script, download the following files:

- [`yolov3.cfg`](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [`yolov3.weights`](https://pjreddie.com/media/files/yolov3.weights)
- [`coco.names`](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

Place them in the same folder as the Python script, or update their paths in the script.

## 🖼️ How to Run

1. Make sure the paths in `yolov3_object_detection.py` point to:
   - The correct `.cfg`, `.weights`, and `coco.names` files
   - A valid image file for detection

2. Run the script:

```bash
python yolov3_object_detection.py
```

The script will:
- Load the YOLOv3 model
- Process the input image
- Run object detection
- Print the detected layer outputs and class list

## 🧠 Example Output

```
Classes
['person', 'bicycle', 'car', ...]
Number of Classes == 80
[array of output shape]
```

To visualize results, you can extend the script using:

```python
cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
cv2.putText(img, label, (x, y - 10), font, 0.5, color, 2)
```

## 📸 Input Image

Update this line in the script with your image path:

```python
img = cv2.imread("your_image.jpg")
```

## ✅ To Do

- [ ] Add bounding box drawing for detections
- [ ] Add support for real-time webcam or video input
- [ ] Show confidence scores and detected class labels

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

You can now save this content as `README.md` and push it to your GitHub repo.

Would you like help modifying the Python script to draw the bounding boxes too?
