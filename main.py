from image_collector import get_business_photos
from text_detection import process_images
from street_view_collector import get_street_view_images
from business_collector import get_businesses_with_addresses


location = 'Oxford Road, Manchester'
locations = ['Oxford Street, London', 'London','Victoria Street, London','Westfield Stratford City, London','Tottenham Court Road, London','Strand, London', 'Camden, London']
testlonglat = '51.51592718571898, -0.135371762197761' # Also in Oxford Street, London
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change','bureau de chage','change money','change currency','fx exchange', 'money transfer', 'currency transfer', 'forex transfer', 'foreign transfer']
check_keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange', 'bureau de change','bureau de chage','money chan','oney exchan','exchange','change money','change currency','change forex','change foreign','change bureau','change de','change chage','change chan','change exchan', 'fx exchange', 'fx change', 'money transfer', 'currency transfer', 'forex transfer', 'foreign transfer', 'bureau de transfer','bureau de transfer','bureau change','bureau chage','bureau chan','bureau exchan','bureau de chage','bureau de chan','bureau de exchan', 'fx', 'fx change'] 

# #Testing on business photos which are tagged to be money exchange related then seeing if process_images works as expected
# for loc in locations:
#     get_business_photos(loc,keywords,1000,'business_photos') # Used to validate that process_images works

# process_images(check_keywords,'business_photos','money_exchange_photos') 

# Testing on random images from street view using a long and lat which has a known 
businesses_with_addresses = get_businesses_with_addresses(location,200)
get_street_view_images(businesses_with_addresses,'street_view_photos',90) #last number is the number of images generated
# process_images(check_keywords,'street_view_photos','forex_street_view_photos') 