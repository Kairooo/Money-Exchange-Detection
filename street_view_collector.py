import os
import requests
import creds
import random

api_key = creds.api_key

def update_location(location, max_step_size=0.001):
    # Parse the current location
    lat, lon = map(float, location.split(','))

    # Generate random steps in latitude and longitude directions
    lat_step = random.uniform(-max_step_size, max_step_size)
    lon_step = random.uniform(-max_step_size, max_step_size)

    # Update the latitude and longitude
    new_lat = lat + lat_step
    new_lon = lon + lon_step

    # Create a new location string
    new_location = f"{new_lat},{new_lon}"

    return new_location

def get_street_view_images(location, photo_directory, image_count=50):

    os.makedirs(photo_directory, exist_ok=True)  # Create the directory if it doesn't exist

    # Iterate over different locations within the specified radius
    for i in range(image_count):
        street_view_url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={location}&key={api_key}&source=outdoor'
        street_view_response = requests.get(street_view_url)
        street_view_response.raise_for_status()

        photo_path = os.path.join(photo_directory, f'street_view_photo_{i + 1}.jpg')
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(street_view_response.content)

    
