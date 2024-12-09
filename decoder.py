import base64
import datetime
import os

def save_base64_image(base64_string, output_path):
    """
    Save the base64 encoded string as an image file.
    
    Parameters:
    - base64_string: base64 encoded string.
    - output_path: Path to save the image.
    """
    try:
        decoded_data = base64.b64decode(base64_string)
        with open(output_path, 'wb') as image_file:
            image_file.write(decoded_data)
    except binascii.Error as e:
        print(f"Error decoding base64 string: {e}")

# Take user input of base64
x = input("Enter base64: ")

if ',' in x:
    x = x.split(',')[1]

base64_string = x

# Validate user input
if not base64_string:
    print("Invalid base64 encoded string")
    exit(1)

# Define the output directory
output_dir = "decoded"

# Create a new folder with the current date and time inside the output directory
current_datetime = datetime.datetime.now()
folder_name = current_datetime.strftime("%d-%m-%Y-%H-%M-%S")
new_folder_path = os.path.join(output_dir, folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# Save decoded image
output_path = os.path.join(new_folder_path, "decoded_image.webp")
save_base64_image(base64_string, output_path)