# File extensions problem for CS50 Python course
# File type to convert:
# .gif -> image/gif
# .jpg -> image/jpeg
# .jpeg -> image/jpeg
# .png -> image/png
# .pdf -> application/pdf
# .txt -> text/plain
# .zip -> application/zip

def main():
    user_prompt = "Hi, what is your file extension:"
    user_input = input(user_prompt).lower().strip()
    print(replace(user_input))
    
def replace(user_input):
    if user_input.endswith(".gif"):
        return "image/gif"
    elif user_input.endswith(".jpg"):
        return "image/jpeg"
    elif user_input.endswith(".jpeg"):
        return "image/jpeg"
    elif user_input.endswith(".png"):
        return "image/png"
    elif user_input.endswith(".pdf"):
        return "application/pdf"
    elif user_input.endswith(".txt"):
        return "text/plain"
    elif user_input.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream" 

if __name__ == "__main__":
    main()