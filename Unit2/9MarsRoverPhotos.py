
#IMPORTS
import requests
from PIL import Image
from io import BytesIO

def fetch_rover(base_url, date_to_search, api_key):
    #concatenate a url with the base_url, your api key, and the extra parameters for the desired date
    #This is the format your url request should be:
    #https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY&date=YYYY-MM-DD
    url = base_url+date_to_search+api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    return data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="
#below, paste your NASA API Key.
api_key = "&api_key=sYlxxqiOHE2YgKOxQg9xtXZ6b1pFGF458seVL8Zm"
date_to_search = "2015-06-03"
rover_data = fetch_rover(base_url,date_to_search,api_key)

print(rover_data)
#if the response we get back has a 'url'...
if 'url' in rover_data:
    print("Title:", rover_data['title'])
    print("Date:", rover_data['date'])
    print("Explanation:", rover_data['explanation'])
    print("HD URL:", rover_data.get('hdurl', "Not available"))
    print("URL:", rover_data['url'])

    # Open and display the image
    response = requests.get(rover_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
#otherwise, if it did not have a url...
else:
    print("Error:", rover_data.get('msg', 'Unknown error'))
