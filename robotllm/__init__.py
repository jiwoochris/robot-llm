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

        self.prompt = None

        print("[Start] your AGI Robot. Nice to meet you")

    def input_text(self, prompt: str) -> str:
        # Perform user's query

        self.prompt = prompt

        if self.verbose:
            print(f"[User prompt] : {prompt}")

        chat_or_request = self.chat_or_request(prompt)

        if chat_or_request == "chat":
            response = self.just_talk(prompt)
            return response

        elif chat_or_request == "request":
            response = self.conduct_request(prompt)
            return "Mission accomplished"

        else:
            raise NeitherChatNorRequest("Neither chat nor request")

    def chat_or_request(self, prompt: str) -> str:
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
        # Just talk with user

        instruction = (
            """
        You are AGI robot. Your goal is to call the appropriate functions.
        Your response should be a python code to conduct user's request for exec.
        """
            + "\n\n"
            + self.function_description
        )

        response = self.llm.call(instruction, prompt)

        if self.verbose:
            print("Generated Python code :")
            print(response)

        exec(response)

        return response

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

        return boxes_and_labels

    # actuator

    def explain_result(self, function_name: str, result: str) -> str:
        # Just talk with user

        instruction = f"You are AGI robot. You got the request :\n{self.prompt}\n\nHere is the result of the {function_name} take_picture(). Answer to user."

        response = self.llm.call(instruction, str(result))

        if self.verbose:
            print(f"[Your AGI] : {response}")
