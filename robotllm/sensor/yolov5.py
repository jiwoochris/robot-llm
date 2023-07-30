import cv2
import torch


class YOLOv5:
    def __init__(self, model_name="yolov5s"):
        self.model = torch.hub.load("ultralytics/yolov5", model_name)  # 80 classes

    def process_frame(self, frame):
        # Perform inference
        results = self.model(frame)

        results.print()

        # Initialize list to store bounding boxes and labels
        boxes_and_labels = []

        # Draw the bounding boxes on the original frame
        for *box, conf, cls in results.xyxy[0]:
            label = f"{results.names[int(cls)]}: {conf:.2f}"
            cv2.rectangle(
                frame,
                (int(box[0]), int(box[1])),
                (int(box[2]), int(box[3])),
                (255, 0, 0),
                2,
            )
            cv2.putText(
                frame,
                label,
                (int(box[0]), int(box[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2,
            )

            # Append bounding box and label to the list
            boxes_and_labels.append((box, label))

        return frame, boxes_and_labels
