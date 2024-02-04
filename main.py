from image_collector import get_business_photos
from text_detection import process_images
from street_view_collector import get_street_view_images

location = 'Oxford Street, London'
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change'] 

# keywords must be a list of strings, radius is a number in meters, photo_directory is a string of the directory name
# get_business_photos(location,keywords,1000,'business_photos') # Used to validate that process_images works
# words_to_check must be a list of strings, input_directory is a string of the directory name to check, output_directory is a string of the directory name to move the images to
# process_images(keywords,'business_photos','money_exchange_photos') 

get_street_view_images('51.51592718571898, -0.135371762197761','street_view_photos') 
# process_images(keywords,'street_view_photos','forex_street_view_photos')