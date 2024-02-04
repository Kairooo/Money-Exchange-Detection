from google.cloud import vision
import os

# Check if the image contains any of the specified words if so then return True else return False
def detect_text(image_path, words_to_check):
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        if any(word.lower() in text.description.lower() for word in words_to_check):
            return True

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )

    return False

# Move the images that contain any of the specified words to a new folder
def process_images(words_to_check):
    input_directory = 'business_photos'
    output_directory = 'money_exchange_photos'
    
    os.makedirs(output_directory, exist_ok=True) #Create the directory if it doesn't exist

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_directory, filename)
            if detect_text(image_path, words_to_check):
                output_path = os.path.join(output_directory, filename)
                os.rename(image_path, output_path)
                print(f'The image {filename} contains one of the specified words and has been moved to {output_directory}.')

