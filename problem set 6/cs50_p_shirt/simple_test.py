#!/usr/bin/env python3

print("Starting simple test...")

try:
    from PIL import Image, ImageOps
    print("PIL imported successfully")
    
    # Test opening shirt.png
    shirt = Image.open("shirt.png")
    print(f"Shirt image opened: {shirt.size}")
    
    # Test opening before1.jpg
    before = Image.open("before1.jpg")
    print(f"Before image opened: {before.size}")
    
    print("All tests passed!")
    
except Exception as e:
    print(f"Error: {e}")
    with open('error_log.txt', 'w') as f:
        f.write(f"Error: {e}\n")

