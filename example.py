from robotllm import RobotLLM

from robotllm.controller.llm.openai import OpenAI
from robotllm.sensor.yolov5 import YOLOv5

llm = OpenAI(instruction="You are AGI robot")
yolo = YOLOv5()

main_llm = RobotLLM(llm = llm, yolo = yolo)
# answer = main_llm.input_text("give me some water")
# print(answer)


res = main_llm.capture_and_process()
print(res)