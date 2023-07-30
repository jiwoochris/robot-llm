from robotllm import RobotLLM

from robotllm.controller.llm.openai import OpenAI
from robotllm.sensor.yolov5 import YOLOv5

your_function_description = """
function description
def self.take_picture() -> boxes_and_labels :str (Yolo)
def self.explain_result(function_name, result) -> explain :str
"""


llm = OpenAI()
yolo = YOLOv5()

main_llm = RobotLLM(
    function_description=your_function_description, llm=llm, yolo=yolo, verbose=True
)
answer = main_llm.input_text("What is in front of me now?")
