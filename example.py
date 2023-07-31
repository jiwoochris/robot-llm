from robotllm import RobotLLM

from robotllm.controller.llm.openai import OpenAI
from robotllm.sensor.yolov5 import YOLOv5

your_function_description = """
function description which robot can use:
def self.take_picture() -> boxes_and_labels (Yolo)
    return [([tensor(263.54340), tensor(72.13196), tensor(633.35150), tensor(476.66077)], 'person: 0.87'), ([tensor(99.12096), tensor(404.57040), tensor(284.40735), tensor(480.)], 'bed: 0.32')]
def self.explain_result(function_name, result) -> explain :str
"""

# def follow_up_question(self, result: str) -> any follow-up question :str:

llm = OpenAI()
yolo = YOLOv5()

main_llm = RobotLLM(
    function_description=your_function_description, llm=llm, yolo=yolo, verbose=True
)

while True:
    user_input = input("[You] : ")  # "how many people is here?"
    answer = main_llm.input_text(user_input)
    print(f"[Your AGI] : {answer}\n")
