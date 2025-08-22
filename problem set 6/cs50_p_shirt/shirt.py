"""
expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

The program should exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input's and output's names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input's name does not have the same extension as the output's name, or
if the specified input does not exist.
"""

import sys
import os
from PIL import Image, ImageOps

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check file extensions
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()
    
    valid_extensions = ['.jpg', '.jpeg', '.png']
    
    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    
    # Check if extensions match
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        sys.exit("Input does not exist")
    
    try:
        # Open the input image
        input_image = Image.open(input_file)
        
        # Open the shirt image
        shirt_image = Image.open("shirt.png")
        
        # Resize and crop input image to match shirt size
        input_image = ImageOps.fit(input_image, shirt_image.size)
        
        # Paste shirt onto the input image
        input_image.paste(shirt_image, (0, 0), shirt_image)
        
        # Save the result
        input_image.save(output_file)
        
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except Exception as e:
        sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
    main()

