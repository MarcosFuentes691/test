import json
import openai
import time

# Assuming you've set your OpenAI API key in the Lambda environment variables
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to create a run and check its status until completion
def create_and_wait_for_run(thread_id, assistant_id):
    client = openai.OpenAI()
    start_time = time.time()  # Record the start time

    # Create the initial thread message
    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content="""Hello doctor, I came here to talk about Cosentyx, do you have a few minutes""",
    )

    # Create the run with additional instructions
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        additional_instructions=" - Answer with 'Yes, I have a few minutes. What would you like to discuss about Cosentyx?'"
    )

    # Check the run status in a loop
    while True:
        # Fetch the latest status of the run
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run_status.status == 'completed':
            thread_messages = client.beta.threads.messages.list(thread_id)
            break
        elif run_status.status == 'failed':
            break
        else:
            continue

    end_time = time.time()  # Record the end time
    duration = end_time - start_time
    return f"Run completed in {duration} seconds."

def lambda_handler(event, context):
    # Example usage
    client = openai.OpenAI()
    thread = client.beta.threads.create()
    thread_id = thread.id
    assistant_id = "asst_xGgF26G4a7BDMGZsA84D1b4s"  # Ensure this is your assistant ID
    result = create_and_wait_for_run(thread_id, assistant_id)
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
