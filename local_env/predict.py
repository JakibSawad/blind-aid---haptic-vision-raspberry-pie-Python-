from collections import Counter
from ultralytics import YOLO


model = YOLO('yolov8n.pt')

source = '/home/sakibjawad/Downloads/299 project/mypicture.jpg'

predictions = model(source, save_txt=None)

# Count occurrences of each class
class_counts = Counter(predictions[0].boxes.cls.tolist())

with open("predicted_labels.txt", '+w') as file:
    for cls, count in class_counts.items():
        class_name = model.names[cls]

        # Write line to file in YOLO label format : cls x y w h
        file.write(f"{count} {class_name} ")
