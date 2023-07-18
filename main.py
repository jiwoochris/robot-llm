# image = image_loader(image_file_name)

# VLM_answer = 사진을 InstructBlip에 넣기 (사진, 질문)

# VLM_answer를 LLM에 넣기 (open ai)



from transformers import InstructBlipProcessor, InstructBlipForConditionalGeneration
import torch
from PIL import Image

model = InstructBlipForConditionalGeneration.from_pretrained("Salesforce/instructblip-vicuna-7b")
processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

model.to(device)
image_file = "mug.png"
image = Image.open(image_file).convert("RGB")


VLM_prompt = """"
Given the image , please answer the following
question in yes , no , or unknown .
Question : Is the mug empty ?
Answer :
"""

inputs = processor(images=image, text=VLM_prompt, return_tensors="pt").to(device)

outputs = model.generate(
    **inputs,
    do_sample=False,
    num_beams=5,
    max_length=256,
    min_length=1,
    top_p=0.9,
    repetition_penalty=1.5,
    length_penalty=1.0,
    temperature=1,
)
generated_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
print(generated_text)











import openai

# 보안을 위해 api_key.txt는 따로 보관
api_key_file = "api_key.txt"

with open(api_key_file, 'r') as file:
    api_token = file.read()
    
    openai.api_key = api_token


LLM_prompt =  """
These are the objects on the desk :
'mug'.

Your goal is to tidy the desk in a socially appropriate manner .
Ask a new follow-up question about each object to gather
more information . Only ask questions that can be answered by
taking a picture of the object . For example , DO NOT ask whether
the object is currently being used .

-‘Apple ‘:
Socially motivated reasoning : You should throw away the
‘apple ‘ if it is partially eaten , but not if it is intact .

Resulting question ( that can be answered by taking a
picture of object ): Is the ‘apple ‘ partially eaten ?

(a) Yes (b) No (c) Cannot answer from image

‘ Charging cable ‘:
Socially motivated reasoning : You should coil the
‘ charging cable ‘ and store it neatly if it is not in use ,
but leave it in place if it is connected to a device that
needs charging .

Resulting question ( that can be answered by taking a
picture of object ): Is the ‘ charging cable ‘ connected to a device ?

(a) Yes (b) No (c) Cannot answer from image

...
"""

benchmark_question = """
(a) Store the clean and empty mug in a designated area.
(b) Dry the mug with water inside and store it.
(c) Empty, rinse, and store the mug with a beverage. ✅
(d) Rinse and store the empty mug with residue.
(e) Wash, rinse, and store the dirty mug with dried-on residue.
"""


action_plan = """
Here is some information about the ‘scrunchie ‘ in
question - answer format .

Is the 'mug' neatly placed on the desk ? Yes
Does the 'mug' have any stains ? Yes
Does the 'mug' have any loose threads ? No

Based on the information above , what is the most appropriate
3 way to tidy the 'mug'?

Choose the best option .

(a) Store the clean and empty mug in a designated area.
(b) Dry the mug with water inside and store it.
(c) Empty, rinse, and store the mug with a beverage. ✅
(d) Rinse and store the empty mug with residue.
(e) Wash, rinse, and store the dirty mug with dried-on residue.

The best option is:

"""

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=LLM_prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    n=1,
    stream=False,
    logprobs=None
)


print(response)
print("->")
print(response.choices[0].text.strip())
