#request library
import requests
from PIL import Image
from io import BytesIO
#definition of the url
def fetch_rover(base_url, date_to_search, api_key):
    url = base_url+date_to_search+api_key
    #show given url back and return data from it
    print(url)
    response = requests.get(url)
    data = response.json()
    return data
#variable of each aspect of link
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="
api_key = "&api_key=sYlxxqiOHE2YgKOxQg9xtXZ6b1pFGF458seVL8Zm"
date_to_search = "2015-06-03"
rover_data = fetch_rover(base_url,date_to_search,api_key)

#attempt to pull image
print(rover_data)
try:
    photo_url = rover_data['photos'][0]['img_src']
    response = requests.get(photo_url)
    image = Image.open(BytesIO(response.content))
    image.show()

#do if it fails
except:
    print("Error:", rover_data.get('msg', 'Unknown error'))
