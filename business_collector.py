import requests
import creds    
import json

def get_businesses_with_addresses(location,size):
    # Initialize an empty list to store business information
    api_key = creds.ch_api_key
    businesses_with_addresses = []

    # Define the search parameters
    url = "https://api.company-information.service.gov.uk/advanced-search/companies"
    params = {
        "location": location,
        "size": str(size),  # You can adjust the size based on your needs
        "start_index": "0"
    }
    # Make the API request
    response = requests.get(url, params=params, auth=(api_key, ''))
    json_search_result = response.text
    data = json.JSONDecoder().decode(json_search_result)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant information (e.g., names and addresses) from the response
        for item in data.get('items', []):
            company_name = item.get('company_name')
            address = item.get('registered_office_address', {})
            address_parts = [
                address.get('address_line_1'),
                address.get('address_line_2'),
                address.get('locality'),
                address.get('postal_code'),
                address.get('country')
            ]
            # Filter out None values and join the parts with a comma
            address_str = ', '.join(filter(None, address_parts))
            businesses_with_addresses.append({'name': company_name, 'address': address_str})
    else:
        print(f'Error: {response.status_code}')
    
    # Return the list of businesses with addresses
    return businesses_with_addresses

