import cv2
from typing import Optional
from .exceptions import NeitherChatNorRequest


class RobotLLM:
    def __init__(
        self,
        llm=None,
        yolo=None,
        verbose: bool = False,
        function_description: Optional[str] = None,
    ):
        self.function_description = function_description
        self.llm = llm
        self.yolo = yolo
        self.verbose = verbose

        self.prompt = ""

        print("[Start] your AGI Robot. Nice to meet you")

    def input_text(self, prompt: str) -> str:
        # Perform user's query

        self.prompt += "\nUser: " + prompt

        if self.verbose:
            print(f"[User prompt] : {self.prompt}")

        chat_or_request = self.check_chat_or_request(prompt)

        if chat_or_request == "chat":
            response = self.just_talk(prompt)

        elif chat_or_request == "request":
            response = self.conduct_request(prompt)

        else:
            raise NeitherChatNorRequest("Neither chat nor request")

        if response == "Mission accomplished":
            self.prompt = ""
        else:
            self.prompt += "\nAGI: " + response

        return response

    def check_chat_or_request(self, prompt: str) -> str:
        instruction = "You are AGI robot. Decide whether user prompt is just chat or request. Your response should be only 'chat' or 'request'"

        response = self.llm.call(instruction, prompt)

        if self.verbose:
            print(f"Chat or Request? : {response}")

        return response

    def just_talk(self, prompt: str) -> str:
        # Just talk with user

        instruction = "You are AGI robot. Be super kind."

        response = self.llm.call(instruction, prompt)

        if self.verbose:
            print(response)

        return response

    def conduct_request(self, prompt: str) -> str:
        instruction = (
            """You are AGI robot. Your goal is to call the appropriate functions.
Your response must be a python code to conduct user's request for exec.
Or If any, ask follow-up question to user.

eg. : What is in front of me now?
result = self.take_picture()
explanation = self.explain_result("take_picture", result)
"""
            + "\n\n"
            + self.function_description
        )

        response = self.llm.call(instruction, prompt)

        if self.verbose:
            print("Respond to request :")
            print(response)

        if self.is_python_code(response):
            exec(response)
            return "Mission accomplished"
        else:
            return response  # eg. Sorry, I am not able to physically tidy a desk as I am an AI assistant. Is there anything else I can help you with?

    def chat_or_request(self, prompt: str) -> str:
        instruction = "You are AGI robot. Decide whether user prompt is just chat or request. Your response should be only 'chat' or 'request'"

        response = self.llm.call(instruction, prompt)

        if self.verbose:
            print(f"Chat or Request? : {response}")

        return response

    def is_python_code(self, code_str):
        try:
            compile(code_str, "<string>", "exec")
            return True
        except SyntaxError:
            return False

    # sensor

    def take_picture(self):
        if self.verbose:
            print("Take picture with Webcam")

        cap = cv2.VideoCapture(0)

        # Read the current frame
        ret, frame = cap.read()

        if ret:
            # Process the frame
            frame, boxes_and_labels = self.yolo.process_frame(frame)

            # Display the frame
            cv2.imshow("Webcam", frame)
            cv2.waitKey(0)  # Wait for any key to be pressed

        # Release the webcam and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

        print(boxes_and_labels)

        return boxes_and_labels

    # actuator

    def explain_result(self, function_name: str, result: str) -> str:
        # Just talk with user

        instruction = f"""You are AGI robot. You got the request :
{self.prompt}
        
Here is the result of the {function_name} take_picture(). Answer to user."""

        if self.verbose:
            print("instruction :")
            print(instruction)

        response = self.llm.call(instruction, str(result))

        if self.verbose:
            print(f"[Your AGI] : {response}")
