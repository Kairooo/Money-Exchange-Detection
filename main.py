from image_collector import get_business_photos
from text_detection import process_images
from street_view_collector import get_street_view_images

location = 'Oxford Street, London'
testlonglat = '51.51592718571898, -0.135371762197761' # Also in Oxford Street, London
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change','oney exchang','exchange'] 

#Testing on business photos which are tagged to be money exchange related then seeing if process_images works as expected
get_business_photos(location,keywords,1000,'business_photos') # Used to validate that process_images works
process_images(keywords,'business_photos','money_exchange_photos') 

# Testing on random images from street view using a long and lat which has a known 
get_street_view_images(testlonglat,'street_view_photos',100) #last number is the number of images generated
process_images(keywords,'street_view_photos','forex_street_view_photos') 