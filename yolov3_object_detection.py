import cv2
import numpy as np

classes = []

with open(r"D:\Computer Vision\yolov3_object_detection\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
    print("Classes \n", classes)
    print("Number of Classes == ", len(classes))

net = cv2.dnn.readNet(r"D:\Computer Vision\yolov3_object_detection\yolov3.weights",
                      r"D:\Computer Vision\yolov3_object_detection\yolov3.cfg")

lay_names = net.getLayerNames()

print(net.getUnconnectedOutLayers())

output_layers = [lay_names[i[0] - 1] for i in net.getUnconnectedOutLayers()] 
print(output_layers)

colors = np.random.uniform(0, 255, size=(len(classes), 3))

img = cv2.imread(r"D:\Computer Vision\yolov3_object_detection\pexels-elevate-1267244.jpg")  

height, width, channels = img.shape

blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

net.setInput(blob)
outs = net.forward(output_layers)
print(outs[2].shape)
print(outs[0][0])




# import cv2
# import numpy as np

# classes = []

# with open(r"D:\Computer Vision\yolov3_object_detection\coco.names", "r") as f:
#   classes = [line.strip() for line in f.readlines()]
#   print("Classes \n", classes)
#   print("Number of Classes == ", len(classes))

# net = cv2.dnn.readNet(r"D:\Computer Vision\yolov3_object_detection\yolov3.weights",
#                       r"D:\Computer Vision\yolov3_object_detection\yolov3.cfg")

# lay_names = net.getLayerNames()

# if isinstance(net.getUnconnectedOutLayers(), list):
#   output_layers = [lay_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# else:
#   output_layers = [lay_names[net.getUnconnectedOutLayers() - 1]]

# print(output_layers)

# colors = np.random.uniform(0, 255, size=(len(classes), 3))

# img = cv2.imread(r"D:\Computer Vision\yolov3_object_detection\pexels-elevate-1267244.jpg")

# height, width, channels = img.shape

# blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# net.setInput(blob)
# outs = net.forward(output_layers)
# print(outs[2].shape)
# print(outs[0][0])
