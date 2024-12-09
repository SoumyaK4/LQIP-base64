from PIL import Image, ImageFilter
import base64
import pyperclip
import tkinter as tk
from tkinter import filedialog
import os
import shutil 

def image_lqip(image_path, output_image_path, length=16, width=8, radius=2):
    """
    Generate a Low-Quality Image Placeholder (LQIP) and save it to a file, then return the base64 encoded string.

    Parameters:
    - image_path: Path to the original image file.
    - output_image_path: Path to save the LQIP file.
    - length: Length of the adjusted image, default is 16.
    - width: Width of the adjusted image, default is 8.
    - radius: Radius of Gaussian blur, default is 2.

    Return:
    - Base64 encoded string.
    """
    im = Image.open(image_path)
    im = im.resize((length, width))
    im = im.convert('RGB')
    im2 = im.filter(ImageFilter.GaussianBlur(radius))  # Gaussian blur
    im2.save(output_image_path)  # save image

    # Convert to base64 encoding
    with open(output_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_string = encoded_string.decode('utf-8')

    return base64_string

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # hide the Tkinter window
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .gif .bmp")])
    if file_path:
        try:
            img = Image.open(file_path)
            return file_path
        except IOError:
            print("Invalid image file")
            return None

def import_image(image_path):
    import_dir = "inputs"
    if not os.path.exists(import_dir):
        os.makedirs(import_dir)
    filename = os.path.basename(image_path)
    import_path = os.path.join(import_dir, filename)
    shutil.copy(image_path, import_path)
    return import_path

def export_demo(image_path, output_filename):
    export_dir = "outputs"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    export_path = os.path.join(export_dir, output_filename)
    shutil.copy(image_path, export_path)
    return export_path

def main():
    print("\n<<<<|  Please select an image to make LQIP  |>>>>")
    image_path = select_image_file()
    if image_path:
        import_path = import_image(image_path)
        print("\nSelected image is imported to: " + import_path + "\n")
        # outputs
        output_path = export_demo(import_path, os.path.splitext(os.path.basename(import_path))[0] + "_demo.jpg")
        base64_image = image_lqip(import_path, output_path)
        output_filename = os.path.splitext(os.path.basename(import_path))[0] + "_lqip.txt"
        output_file_path = os.path.join("outputs", output_filename)
        with open(output_file_path, "w") as f:
            f.write('data:image/jpg;base64,' + base64_image)
        pyperclip.copy(base64_image)  # Copy the result into the clipboard.
        print(base64_image + "\n\nLQIP exported to: " + output_file_path + " , and also copied to the clipboard.\nLQIP preview demo here: " + output_path)

if __name__ == "__main__":
    main()