import subprocess
import time
import datetime

def run_script(script_name):
    """Function to run a Python script and return its output."""
    output = ""
    try:
        # Run the script
        completed_process = subprocess.run(['python3', script_name], check=True, text=True, capture_output=True)
        # Gather the standard output of the script
        output = f"Output of {script_name}:\n{completed_process.stdout}\n"
    except subprocess.CalledProcessError as e:
        # If the script returns a non-zero exit status, an error occurred.
        output = f"Error running {script_name}:\n{e.output}\n"
    return output

if __name__ == "__main__":
    # List of scripts to run
    scripts = ['script.py', 'chunk.py', 'normal.py']
    
    while True:  # This creates an infinite loop to keep the script running
        outputs = []  # Initialize a list to store outputs
        
        current_time = datetime.datetime.now()  # Get the current time
        # Store the current time in a readable format
        outputs.append(f"Running scripts at {current_time.strftime('%Y-%m-%d %H:%M:%S')}...\n")
        print(f"Running scripts at {current_time.strftime('%Y-%m-%d %H:%M:%S')}...")  # Also print this to the console
        
        # Iterate over the list of scripts and run each one
        for script in scripts:
            outputs.append(f"Running {script}...\n")
            print(f"Running {script}...")  # Print to console
            script_output = run_script(script)
            outputs.append(script_output)  # Store the script output
            outputs.append(f"Finished running {script}.\n\n")
            print(f"Finished running {script}.\n")  # Also print this to the console
        
        # Store the final output indicating all scripts have finished
        outputs.append(f"Finished all scripts at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        outputs.append("Waiting for one hour before the next run...\n\n")
        print("Finished all scripts.\nWaiting for one hour before the next run...\n")  # Print to console
        
        # Write all outputs to the file at once
        with open('script_outputs.txt', 'a') as file:
            file.writelines(outputs)
        
        time.sleep(3600)  # Wait for 3600 seconds (1 hour) before the next run