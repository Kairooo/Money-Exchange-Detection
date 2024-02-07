# Money Exchange Detection
 Detecting Money Exchange businesses without license.

## About The Tool
 As the name suggests this tool will first generate pictures of businesses and checks if it is a money exchange business with a license or not.

## How it works
 It uses the Places API to get pictures in the area of a given location. It will get pictures then check if it is a money exchange business by using Vision API to detect what text it has in front of the business. We will save the locations of businesses which are detected as a money exchange business. We will check if the businesses at this location is certified and if not then we will save these businesses.

 ## Setup
 - Download or clone the repository
 - Get API key by going to [Google Cloud Console](https://console.cloud.google.com/welcome/new?hl=en) 
 - Add a creds.py file to the repository and write api_key = [INSERT YOUR API KEY] in that file 
 - Setup Cloud Vision by going to [Cloud Vision Setup](https://cloud.google.com/vision/docs/setup)
 - We are good to go! run main.py!