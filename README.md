# Money Exchange Detection
Detecting Money Exchange businesses without license.

## About The Tool
As the name suggests this tool will first generate pictures of businesses and check if it is a licensed money exchange business.

## How it works
It uses the Places API to get pictures in the area of a given location. It will get pictures and then check if it is a money exchange business by using Vision API to detect what text it has in front of the business. We will save the locations of businesses detected as a money exchange business. We will check if the businesses at this location are certified; if not, we will save these businesses. (STILL IN PROGRESS)

 ## Setup
 - Download or clone the repository
 - Get the GCP API key by going to [Google Cloud Console](https://console.cloud.google.com/welcome/new?hl=en) 
 - Add a creds.py file to the repository and write gcp_api_key = 'YOUR_API_KEY' in that file 
 - Setup Cloud Vision by going to [Cloud Vision Setup](https://cloud.google.com/vision/docs/setup)
 - Get the Companies House API key by going to [Companies House Setup](https://developer-specs.company-information.service.gov.uk/guides/gettingStarted) and following the guide making sure to use a live application instead of a test application and getting a REST key.
 - Add ch_api_key = 'YOUR_API_KEY' to creds.py 
 - We are good to go! run main.py!
