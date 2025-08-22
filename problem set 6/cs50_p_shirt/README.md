# CS50 P-Shirt

## Overview
This program overlays a virtual CS50 t-shirt onto photos. After finishing CS50, students traditionally receive their "I took CS50" t-shirt. This program allows you to try one on virtually!

## Requirements
The program expects exactly two command-line arguments:
- `sys.argv[1]`: Name/path of a JPEG or PNG to read as input
- `sys.argv[2]`: Name/path of a JPEG or PNG to write as output

## Functionality
1. **Input Validation**: Checks for exactly two arguments
2. **File Extension Validation**: Ensures both files end in .jpg, .jpeg, or .png (case-insensitive)
3. **Extension Matching**: Input and output must have the same extension
4. **File Existence**: Verifies input file exists
5. **Image Processing**: 
   - Opens input image with PIL.Image.open
   - Resizes and crops input to match shirt.png dimensions using PIL.ImageOps.fit
   - Overlays shirt.png (with transparent background) onto the input
   - Saves the result

## Error Handling
The program exits via `sys.exit` with appropriate error messages for:
- Too few/many command-line arguments
- Invalid file extensions
- Mismatched extensions between input/output
- Non-existent input file

## Dependencies
- `PIL` (Pillow) library for image processing
- `sys` for command-line arguments
- `os` for file existence checks

## Usage Examples
```bash
# Basic usage
python3 shirt.py before1.jpg after1.jpg

# Test error cases
python3 shirt.py                    # Too few arguments
python3 shirt.py before1.jpg        # Too few arguments  
python3 shirt.py before1.jpg before2.jpg before3.jpg  # Too many arguments
python3 shirt.py before1.jpg invalid.bmp  # Invalid output format
python3 shirt.py before1.jpg after1.png   # Different extensions
python3 shirt.py nonexistent.jpg after1.jpg  # File doesn't exist
```

## Testing
The program has been tested with the CS50 muppets dataset:
- `before1.jpg`, `before2.jpg`, `before3.jpg` - Input photos
- `shirt.png` - CS50 t-shirt overlay template (600x600 PNG with transparency)

## CS50 Check50 Results
✅ All tests passed successfully!

## Files
- `shirt.py` - Main program
- `shirt.png` - CS50 t-shirt overlay template
- `before1.jpg`, `before2.jpg`, `before3.jpg` - Sample input images
- `muppets.zip` - Original dataset from CS50

## Submission
This exercise is ready for submission to CS50 using:
```bash
submit50 cs50/problems/2022/python/shirt
```

## Learning Outcomes
- Command-line argument processing with `sys.argv`
- Image manipulation using PIL/Pillow
- File validation and error handling
- Working with transparent PNG images
- Using `ImageOps.fit` for resizing and cropping

