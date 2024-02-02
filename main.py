import os
import requests
import creds

api_key = creds.api_key
location = 'Tottenham Court Road, London'
radius = 10000  # 1km for now but can be adjusted later
keywords = ['money exchange', 'currency exchange', 'forex', 'foreign exchange']



# Process the results and store in a database
business_database = []

# Create a directory to save photos if it doesn't exist
photo_directory = 'business_photos'
os.makedirs(photo_directory, exist_ok=True)

for keyword in keywords:
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}+in+{location}&radius={radius}&key={api_key}'
    response = requests.get(url)
    results = response.json().get('results', [])

    for result in results:
        business_data = {
            'name': result.get('name', ''),
            'address': result.get('formatted_address', ''),
            'types': result.get('types', []),
            'photo_reference': result.get('photos', [])[0].get('photo_reference', '') if result.get('photos') else ''
            # Add more fields as needed
        }
        business_database.append(business_data)

for entry in business_database:
    if entry['photo_reference']:
        photo_filename = f'{entry["name"].replace(" ", "_").replace("/", "_")}_photo.jpg'
        photo_path = os.path.join(photo_directory, photo_filename)
        photo_url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={entry["photo_reference"]}&key={api_key}'
        photo_response = requests.get(photo_url)
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(photo_response.content)
