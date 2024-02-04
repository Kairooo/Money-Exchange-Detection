import os
import requests
import creds

api_key = creds.api_key

def get_business_photos(location, keywords, radius, photo_directory):
    business_database = []
    os.makedirs(photo_directory, exist_ok=True) #Create the directory if it doesn't exist

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
