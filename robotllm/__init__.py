import cv2


class RobotLLM:
    def __init__(self, llm=None, yolo=None, verbose: bool = False):
        self.llm = llm
        self.yolo = yolo
        self.verbose = verbose

        print("Start your AGI Robot. Nice to meet you")

    def input_text(self, prompt: str) -> str:
        # Perform user's query

        completion = self.llm.call(prompt)
        respond = completion.choices[0].message.content.strip()

        if self.verbose:
            print(completion)
            print("->")
            print(respond)

        return respond

    # sensor

    def capture_and_process(self):
        cap = cv2.VideoCapture(0)

        # Read the current frame
        ret, frame = cap.read()

        if ret:
            # Process the frame
            frame = self.yolo.process_frame(frame)

            # Display the frame
            cv2.imshow("Webcam", frame)
            cv2.waitKey(0)  # Wait for any key to be pressed

        # Release the webcam and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

    # actuator
