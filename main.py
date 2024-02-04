from image_collector import get_business_photos
from text_detection import process_images
import creds

location = 'Oxford Street, London'
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change'] 

# keywords must be a list of strings, radius is a number in meters, photo_directory is a string of the directory name
get_business_photos(location,keywords,1000,'business_photos') 
# words_to_check must be a list of strings, input_directory is a string of the directory name to check, output_directory is a string of the directory name to move the images to
process_images(keywords,'business_photos','money_exchange_photos') 