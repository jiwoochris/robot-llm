import openai

# 보안을 위해 api_key.txt는 따로 보관
api_key_file = "api_key.txt"

with open(api_key_file, "r") as file:
    api_token = file.read()

    openai.api_key = api_token


LLM_prompt = """
These are the objects on the desk :
'mug'.

Your goal is to tidy the desk in a socially appropriate manner .
Ask a new follow-up question about each object to gather
more information . Only ask questions that can be answered by
taking a picture of the object . For example , DO NOT ask whether
the object is currently being used .

-‘Apple ‘:
Socially motivated reasoning : You should throw away the ‘apple ‘ if it is partially eaten , but not if it is intact .

Resulting question ( that can be answered by taking a picture of object ): Is the ‘apple ‘ partially eaten ?

(a) Yes (b) No (c) Cannot answer from image

‘ Charging cable ‘:
Socially motivated reasoning : You should coil the ‘ charging cable ‘ and store it neatly if it is not in use , but leave it in place if it is connected to a device that needs charging .

Resulting question ( that can be answered by taking a picture of object ): Is the ‘ charging cable ‘ connected to a device ?

(a) Yes (b) No (c) Cannot answer from image

...
"""


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=LLM_prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    n=1,
    stream=False,
    logprobs=None,
)


print(response)
print("->")
print(response.choices[0].text.strip())

answer1 = response.choices[0].text.strip()


import re

match = re.search(
    r"Resulting question \( that can be answered by taking a picture of object \): (.*?)\n\n",
    answer1,
    re.DOTALL,
)

print(match)

if match:
    question = match.group(1)
    print(question)


# No라고 가정하자
answer_to_LLM_question = "No"


action_plan = f"""
Here is some information about the ‘scrunchie ‘ in
question - answer format .

{question} {answer_to_LLM_question}

Based on the information above , what is the most appropriate
3 way to tidy the 'mug'?

Choose the best option .

(a) Store the clean and empty mug in a designated area.
(b) Dry the mug with water inside and store it.
(c) Empty, rinse, and store the mug with a beverage.
(d) Rinse and store the empty mug with residue.
(e) Wash, rinse, and store the dirty mug with dried-on residue.

The best option is:

"""


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=action_plan,
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    n=1,
    stream=False,
    logprobs=None,
)


print(response)
print("->")
print(response.choices[0].text.strip())
