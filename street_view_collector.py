import os
import requests
import creds

def get_street_view_images(businesses_with_addresses, photo_directory,fov):
    api_key = creds.gcp_api_key
    os.makedirs(photo_directory, exist_ok=True)  # Create the directory if it doesn't exist

    # Iterates through the number of images requested and saves them to the photo_directory
    for business in businesses_with_addresses:

        location = business["address"]
        street_view_url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={location}&key={api_key}&fov={fov}&size=640x640&source=outdoor'
        street_view_response = requests.get(street_view_url)
        street_view_response.raise_for_status()
            
        # Save the image
        with open(os.path.join(photo_directory, f'{business["name"]}.jpg'), 'wb') as f:
            f.write(street_view_response.content)

    
