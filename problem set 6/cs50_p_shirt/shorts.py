from PIL import Image

def main():
    with Image.open("shirt.png") as shirt:
        print(shirt.size)
        print(shirt.format)


main()