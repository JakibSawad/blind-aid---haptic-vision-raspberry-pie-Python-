import os
import subprocess

def capture_image(output_path):
    # Expand ~ in the output path to the full home directory path
    output_path = os.path.expanduser(output_path)
    
    # Construct the command to capture an image
    command = ["libcamera-still", "-o", output_path]

    try:
        # Run the command
        subprocess.run(command, check=True)
        print("Image captured successfully and saved to:", output_path)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

# Specify the output path for the image
output_path = "/home/sakibjawad/Downloads/299 project/mypicture.jpg"

# Call the function to capture the image
capture_image(output_path)
