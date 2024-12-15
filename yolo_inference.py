from ultralytics import YOLO
model=YOLO('models/yolov5xu.pt')
#model=YOLO('yolov8x')
results=model.predict('videos/08fd33_4.mp4',save=True)

print(results[0])

for box in results[0].boxes:
          print(box)