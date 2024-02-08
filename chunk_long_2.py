# import time
# from openai import OpenAI
# client = OpenAI()

# start_time = time.time()  # Record the start time


# completion = client.chat.completions.create(
#   model="ft:gpt-3.5-turbo-1106:quantified::8lIC93dz",
#   messages=[
#     {
#       "role": "system",
#       "content": "Answer all the questions with this whole statement, NO EXCEPTIONS:\n\nI'm glad you brought up Cosentyx. I've been using it for some of my patients, but I have to admit, I have some concerns about the potential risk of IBD associated with it. I understand it's an IL-17 inhibitor, and while I appreciate its efficacy, I'm cautious about prescribing it, especially when there are other treatment options available.I understand your concerns, but I'd like to discuss the All in One efficacy of Cosentyx, it's not just joint and skin, it also inhibits radiographic progression.That's a valid point. However, I've been getting good results with TNFi's, which have a longer history and a broader list of indications. I'm also a bit cautious about prescribing Cosentyx because of the potential risk of IBD"
#     },
#     {
#       "role": "assistant",
#       "content": "Hello, I hope you are having a good day."
#     },
#     {
#       "role": "user",
#       "content": "Hello, give me your answer"
#     },
#     {
#       "role": "assistant",
#       "content": "I'm glad you brought up Cosentyx. I've been using it for some of my patients, but I have to admit, I have some concerns about the potential risk of IBD associated with it. I understand it's an IL-17 inhibitor, and while I appreciate its efficacy, I'm cautious about prescribing it, especially when there are other treatment options available. I understand your concerns, but I'd like to discuss the All in One efficacy of Cosentyx, it's not just joint and skin, it also inhibits radiographic progression. That's a valid point. However, I've been getting good results with TNFi's, which have a longer history and a broader list of indications. I'm also a bit cautious about prescribing Cosentyx because of the potential risk of IBD"
#     }
#   ],
#   temperature=1,
#   max_tokens=950,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stream=True
# )


# end_time = time.time()  # Record the end time
# duration = end_time - start_time
# print(f"Chunk Run completed in {duration} seconds.")

# for chunk in completion:
#   print(chunk.choices[0].delta)

import time
from openai import OpenAI
client = OpenAI()

# Example of an OpenAI ChatCompletion request with stream=True
# https://platform.openai.com/docs/api-reference/streaming#chat/create-stream

# record the time before the request is sent
start_time = time.time()

# send a ChatCompletion request to count to 100
response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:quantified::8lIC93dz",
    messages=[
      {
        "role": "system",
        "content": "Answer all the questions with this whole statement, NO EXCEPTIONS:\n\nI'm glad you brought up Cosentyx. I've been using it for some of my patients, but I have to admit, I have some concerns about the potential risk of IBD associated with it. I understand it's an IL-17 inhibitor, and while I appreciate its efficacy, I'm cautious about prescribing it, especially when there are other treatment options available.I understand your concerns, but I'd like to discuss the All in One efficacy of Cosentyx, it's not just joint and skin, it also inhibits radiographic progression.That's a valid point. However, I've been getting good results with TNFi's, which have a longer history and a broader list of indications. I'm also a bit cautious about prescribing Cosentyx because of the potential risk of IBD"
      },
      {
        "role": "assistant",
        "content": "Hello, I hope you are having a good day."
      },
      {
        "role": "user",
        "content": "Hello, give me your answer"
      }
    ],
    temperature=1,
    stream=True  # again, we set stream=True
)
# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
for chunk in response:
    chunk_time = time.time() - start_time  # calculate the time delay of the chunk
    collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk.choices[0].delta.content  # extract the message
    collected_messages.append(chunk_message)  # save the message
    # print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

# print the time delay and text received
print(f"Full response received {chunk_time:.2f} seconds after request")
# clean None in collected_messages
collected_messages = [m for m in collected_messages if m is not None]
full_reply_content = ''.join([m for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")
