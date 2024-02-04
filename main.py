from image_collector import get_business_photos
from text_detection import process_images
import creds

location = 'Oxford Street, London'
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change'] 
get_business_photos(location,keywords,1000) # keywords must be a list of strings, radius is a number in meters
process_images(keywords)