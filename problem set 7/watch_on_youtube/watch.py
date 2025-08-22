# Expects a str of HTML as input, extracts any YouTube URL that's the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str
# Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

def parse(iframe):
    # First check if there is a youtube video in the iframe
    if "youtube" not in iframe:
        return None
    
    # Check if this is actually an iframe with src attribute
    if "iframe" not in iframe or "src" not in iframe:
        return None
    
    # If there is a youtube video, find the video id    
    src_position = iframe.find("src")
    equals_position = iframe.find("=", src_position)
    
    # Check if we found valid positions
    if equals_position == -1:
        return None
        
    quote_position = iframe.find('"', equals_position)
    if quote_position == -1:
        return None
        
    second_quote_position = iframe.find('"', quote_position + 1)
    if second_quote_position == -1:
        return None
        
    embed_position = iframe.find("embed/", quote_position + 1)
    
    # Check if we found "embed/" and it's before the second quote
    if embed_position == -1 or embed_position >= second_quote_position:
        return None
    
    video_id = iframe[embed_position + 6:second_quote_position]
    
    # Additional validation: make sure the video_id looks valid
    if not video_id or len(video_id) < 5:  # YouTube IDs are typically 11 characters
        return None
    
    # CRITICAL: Validate that the URL actually contains "youtube.com/embed/"
    # Extract the full URL to check its structure
    full_url = iframe[quote_position + 1:second_quote_position]
    if not full_url.startswith(("http://", "https://")) or "youtube.com/embed/" not in full_url:
        return None
        
    return "https://youtu.be/" + video_id

if __name__ == "__main__":
    # Get input from user
    iframe = input("Please enter the full HTML/iframe code: ")
    result = parse(iframe)
    print(result)