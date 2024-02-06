import subprocess
import time
import datetime

def run_script(script_name):
    """Function to run a Python script and save its output to a txt file."""
    try:
        # Run the script
        completed_process = subprocess.run(['python3', script_name], check=True, text=True, capture_output=True)
        # Save the standard output of the script to a txt file
        with open('script_outputs.txt', 'a') as file:  # Open the file in append mode
            file.write(f"Output of {script_name}:\n{completed_process.stdout}\n")
        print(f"Output of {script_name} saved to script_outputs.txt")
    except subprocess.CalledProcessError as e:
        # If the script returns a non-zero exit status, an error occurred.
        with open('script_outputs.txt', 'a') as file:  # Open the file in append mode
            file.write(f"Error running {script_name}:\n{e.output}\n")
        print(f"Error running {script_name}:\n{e.output}")

if __name__ == "__main__":
    # List of scripts to run
    scripts = ['script.py', 'chunk.py', 'normal.py']
    
    while True:  # This creates an infinite loop to keep the script running
        current_time = datetime.datetime.now()  # Get the current time
        print(f"Running scripts at {current_time.strftime('%Y-%m-%d %H:%M:%S')}...")  # Print the current time in a readable format
        
        # Iterate over the list of scripts and run each one
        for script in scripts:
            print(f"Running {script}...")
            run_script(script)
            print(f"Finished running {script}.\n")
        
        print(f"Finished all scripts at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Waiting for one hour before the next run...\n")
        time.sleep(3600)  # Wait for 3600 seconds (1 hour) before the next run
