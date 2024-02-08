import time
from openai import OpenAI
client = OpenAI()

start_time = time.time()  # Record the start time


completion = client.chat.completions.create(
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
  max_tokens=950,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stream=True
)

collected_chunks = []
collected_messages = []

# Assuming 'completion' is a list of chunks
for i, chunk in enumerate(completion):
    if i % 25 == 0:  # Check if it's the start of a new group of 10
        if i != 0:  # Avoid printing for the first chunk
            end_time = time.time()  # Record the end time for the group
            duration = end_time - group_start_time
            print(f"Group of 25 chunks processed in {duration} seconds.")
        group_start_time = time.time()  # Reset start time for the next group
    
    collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk.choices[0].delta.content  # extract the message
    collected_messages.append(chunk_message)  # save the message

# After loop, check if there was a last group with less than 10 chunks
if len(completion) % 25 != 0:
    end_time = time.time()  # Record the end time for the last group
    duration = end_time - group_start_time
    print(f"Last group of chunks processed in {duration} seconds.")

# Filter out None messages and concatenate
collected_messages = [m for m in collected_messages if m is not None]
full_reply_content = ''.join([m for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")

# Finally, print the total duration
total_end_time = time.time()
total_duration = total_end_time - start_time
print(f"Total Run completed in {total_duration} seconds.")