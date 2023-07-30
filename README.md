# Robot-LLM: Expanding AGI Capabilities with a Language Learning Model for Robotics 🤖

![robot-llm](https://github.com/juicyjung/robot-llm/assets/83687471/73d74d29-3aa9-465e-8cb8-ddb0e842a34b)


Robot-LLM is a framework for implementing Artificial General Intelligence (AGI) in robots. By combining large language models (LLMs) with versatile sensors and actuators, RobotLLM enables robots to understand complex commands and perceive their environment.

Come, let's create the future of AGI in robotics together!

## 🚀 Quickstart Guide

Follow these steps to get started with the LLM-Vector-database:

**1. Clone the repository** 

Use the following command to clone the repository:

```bash
git clone https://github.com/juicyjung/robot-llm.git
```

**2. Install dependencies** 

This project uses [Poetry](https://python-poetry.org/docs/) for dependency management. If you don't have Poetry installed, you can install it using:

```bash
pip install poetry
```

Then, install the project dependencies:

```bash
poetry install
```

**3. Install PyTorch**

This project relies on PyTorch. You need to install the version of PyTorch appropriate for your system. Refer to the official [PyTorch](https://pytorch.org/get-started/locally/) site for installation details tailored to your needs.

**4. Run the code**

You're all set! Now you can run the provided code or experiment with your own modifications.


## 💻 Usage

Here is an example of how to use this package:

```python
from robotllm import RobotLLM

from robotllm.controller.llm.openai import OpenAI
from robotllm.sensor.yolov5 import YOLOv5

your_function_description = """
function description which robot can use:
def self.take_picture() -> boxes_and_labels (Yolo)
    return [([tensor(263.54340), tensor(72.13196), tensor(633.35150), tensor(476.66077)], 'person: 0.87'), ([tensor(99.12096), tensor(404.57040), tensor(284.40735), tensor(480.)], 'bed: 0.32')]
def self.explain_result(function_name, result) -> explain :str
"""

llm = OpenAI()
yolo = YOLOv5()

main_llm = RobotLLM(
    function_description=your_function_description, llm=llm, yolo=yolo, verbose=True
)

while True:
    user_input = input("[You] : ")  # "how many people is here?"
    answer = main_llm.input_text(user_input)
    print(f"[Your AGI] : {answer}\n")
```


## 🔍 Expanding Your Robot's AGI Capabilities

Adding different sensors and actuators to your robot significantly expands its AGI capabilities. By defining and adding more complex function descriptions, your robot can understand and interact with the world more effectively. For example, you could add a function for a camera sensor to capture images, a function to control a robot arm for precise manipulation or a function for a motor to move the robot.

The possibilities are endless! We are excited to see what you will build with RobotLLM. Happy coding!


## 🦾 How to Add Sensor and Actuator Function Descriptions

RobotLLM is designed to be versatile and flexible. You can add any sensor or actuator function descriptions and it will enable your robot to perform more complex tasks based on your requirements. These functions are the building blocks for your robot's perception and action capabilities. 

Here's how you can add sensor and actuator function descriptions:

1. Define a function description for each sensor or actuator. The function descriptions should be formatted as shown below:

```python
"""
def self.sensor_or_actuator_function_name() -> return_type:
    return ...
"""
```
In the example, `sensor_or_actuator_function_name` should be replaced with the name of your function, `return_type` should be replaced with the type of value your function returns, and the `return ...` statement should be replaced with the actual output of your function.

2. In the main program, use the defined function descriptions to initialize the RobotLLM:

```python
main_llm = RobotLLM(
    function_description=your_function_description, llm=llm, sensor_or_actuator=sensor_or_actuator, verbose=True
)
```

In this example, `sensor_or_actuator` should be replaced with the instance of the sensor or actuator you want to use.

3. Now your robot is ready to use the new sensor or actuator capabilities! You can use the same interaction loop to get inputs from the user and generate appropriate outputs.


## 🤝 Contribution

Contributions are welcome! Please feel free to submit a pull request.

## 📜 License

This project is licensed under the MIT License.
