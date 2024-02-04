import os
import requests
import creds
import random

api_key = creds.api_key

def update_location(location, step_size=0.001, direction='E'):
    # Parse the current location
    lat, lon = map(float, location.split(','))

    # Initialize new_lat and new_lon with current latitude and longitude
    new_lat = lat
    new_lon = lon

    # Update the latitude and longitude based on the direction
    if direction == 'E':
        new_lon = lon + step_size
    elif direction == 'W': # This does the same as 'E' because it would keep going back to where we started and is kept here to avoid repetition in pictures
        new_lon = lon + step_size
    elif direction == 'N':
        new_lat = lat + step_size
    elif direction == 'S':
        new_lat = lat - step_size

    # Create a new location string
    new_location = f"{new_lat},{new_lon}"

    return new_location

def get_street_view_images(location, photo_directory, image_count=50, step_size=0.001):
    os.makedirs(photo_directory, exist_ok=True)  # Create the directory if it doesn't exist

    # Define the directions
    directions = ['N', 'E', 'S', 'W']

    # Iterate over different locations within the specified radius
    for i in range(image_count):

        street_view_url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={location}&key={api_key}&source=outdoor'
        street_view_response = requests.get(street_view_url)
        street_view_response.raise_for_status()

        # Get the direction for this iteration
        direction = directions[i % len(directions)]
        # Update the location
        location = update_location(location, step_size, direction)

        # Save the image
        with open(os.path.join(photo_directory, f'street_view_photo_{i}.jpg'), 'wb') as f:
            f.write(street_view_response.content)

    
