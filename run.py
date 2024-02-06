import subprocess
import time
import datetime

def run_script(script_name):
    """Function to run a Python script and print its output."""
    try:
        # Run the script
        completed_process = subprocess.run(['python3', script_name], check=True, text=True, capture_output=True)
        # Print the standard output of the script
        print(f"Output of {script_name}:\n{completed_process.stdout}")
    except subprocess.CalledProcessError as e:
        # If the script returns a non-zero exit status, an error occurred.
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
