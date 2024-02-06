import json
import openai
import time
from openai import OpenAI
import os

# Assuming you've set your OpenAI API key in the Lambda environment variables
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

# Function to create a run and check its status until completion
def create_and_wait_for_run(thread_id, assistant_id):
    start_time = time.time()  # Record the start time

    thread_message = client.beta.threads.messages.create(
      thread_id,
      role="user",
      content="""Hello doctor, I came here to talk about Cosentyx, do you have a few minutes""",
    )

    # Create the run
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        additional_instructions=" - Answer with 'Yes, I have a few minutes. What would you like to discuss about Cosentyx?'"
    )
    # print(f"Run created with ID: {run.id}")

    # Check the run status in a loop
    i=0
    while True:
        # Fetch the latest status of the run
        run_status = client.beta.threads.runs.retrieve(
          thread_id=thread_id,
          run_id=run.id
        )
        if run_status.status == 'completed':
            # print("Run completed!")
            thread_messages = client.beta.threads.messages.list(thread_id)
            //print(thread_messages.data)
            break
        elif run_status.status == 'failed':
            # print("Run failed!")
            break
        else:
            # i = i+1
            continue
            # print("Run is still processing...")
            # time.sleep(5)  # Wait for 5 seconds before checking again

    end_time = time.time()  # Record the end time
    duration = end_time - start_time
    print(f"Assistants run completed in {duration} seconds.")
    # print(i)

# Example usage
thread = client.beta.threads.create()
# thread_id = "thread_NGEVXzzgcOH2DoA9zptPTWnR"
thread_id = thread.id
# print(thread_id)
assistant_id = "asst_xGgF26G4a7BDMGZsA84D1b4s"
create_and_wait_for_run(thread_id, assistant_id)


