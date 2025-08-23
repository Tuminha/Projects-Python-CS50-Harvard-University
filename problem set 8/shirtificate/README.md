# CS50 Shirtificate

## Overview
The **CS50 Shirtificate** project creates a personalized PDF certificate that looks like a CS50 t-shirt. Users input their name, and the program generates a PDF with a CS50 shirt image and the user's name overlaid on it, creating a custom "shirtificate" commemorating their CS50 experience.

## Learning Objectives
This project demonstrates:
- **PDF Generation**: Using the `fpdf2` library to create PDF documents programmatically
- **Image Manipulation**: Embedding images into PDF documents
- **Text Positioning**: Precise placement of text elements within a PDF layout
- **File I/O**: Reading image files and writing PDF output files
- **User Input Handling**: Collecting and processing user input for personalization

## Features
- **Interactive Name Input**: Prompts the user to enter their name
- **Professional PDF Layout**: Creates a well-formatted certificate with proper spacing
- **Custom Typography**: Uses Helvetica font with different sizes for title and name
- **Image Integration**: Embeds a CS50 shirt image as the background
- **Personalized Message**: Displays "{name} took CS50" on the certificate
- **File Output**: Saves the certificate as `shirtificate.pdf`

## Implementation Details

### Core Components
1. **PDF Creation**: Initializes a new PDF document with `FPDF()`
2. **Page Setup**: Adds a page and sets up the layout structure
3. **Title Generation**: Creates the "CS50 Shirtificate" header in large, bold text
4. **Image Embedding**: Places the shirt image at the center of the document
5. **Name Overlay**: Adds the personalized text over the shirt image
6. **File Export**: Outputs the final PDF to disk

### Technical Specifications
- **Font**: Helvetica (Bold for title, Regular for name)
- **Title Size**: 50pt for "CS50 Shirtificate"
- **Name Size**: 24pt for personalized text
- **Image Format**: PNG (shirtificate.png)
- **Output Format**: PDF (shirtificate.pdf)
- **Text Alignment**: Center-aligned for professional appearance

## Files
- `shirtificate.py` - Main program that generates the PDF certificate
- `shirtificate.png` - CS50 shirt image used as the certificate background
- `shirtificate.pdf` - Generated output file (created when program runs)

## Usage
```bash
python shirtificate.py
```

The program will:
1. Prompt you to enter your name
2. Generate a PDF certificate with your name
3. Save the result as `shirtificate.pdf`

### Example
```
Name: Francisco
```
Output: Creates `shirtificate.pdf` with "Francisco took CS50" text overlaid on the CS50 shirt image.

## Testing
The project passes CS50's automated tests:
- ✅ `shirtificate.py` exists
- ✅ `shirtificate.py` creates a PDF called `shirtificate.pdf`

## Dependencies
```bash
pip install fpdf2
```

## CS50 Integration
This project is part of **CS50's Introduction to Programming with Python**, specifically:
- **Problem Set 8**: Object-Oriented Programming
- **Course**: CS50P
- **Institution**: Harvard University
- **Verification**: `check50 cs50/problems/2022/python/shirtificate`
- **Submission**: `submit50 cs50/problems/2022/python/shirtificate`

## Skills Demonstrated
- PDF library usage (`fpdf2`)
- File handling and output generation
- Image processing and embedding
- Typography and layout design
- User input validation and processing
- Professional document creation

## Educational Value
This project teaches practical skills in document generation, combining programming with design elements to create professional-looking output. It demonstrates how Python can be used beyond simple console applications to generate real-world documents and certificates.
