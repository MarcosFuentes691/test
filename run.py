import subprocess
import time
import datetime

def run_script(script_name):
    """Function to run a Python script and save its output to a txt file."""
    try:
        # Run the script
        completed_process = subprocess.run(['python3', script_name], check=True, text=True, capture_output=True)
        # Save the standard output of the script to a txt file
        with open(script_name + '_output.txt', 'w') as file:
            file.write(completed_process.stdout)
        print(f"Output of {script_name} saved to {script_name}_output.txt")
    except subprocess.CalledProcessError as e:
        # If the script returns a non-zero exit status, an error occurred.
        print(f"Error running {script_name}:\n{e.output}")

if __name__ == "__main__":
    # List of scripts to run
    scripts = ['script.py', 'chunk.py', 'normal.py']
    
    while True:  # This creates an infinite loop to keep the script running
        current_time = datetime.datetime.now()  # Get the current time
        print(f"Running scripts at {current
