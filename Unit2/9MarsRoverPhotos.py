#requests is a library we will use to make HTTP requests
import requests
#PIL stands for "Photo Imaging Library". We will use it to display our image
from PIL import Image
#io means Input/Output. BytesIO allows us to store information and recall it. It is like an advanced variable.
from io import BytesIO

#fetch_apod function makes the request through the internet to get our APOD data
def fetch_rover(base_url, api_key):
    #concatenate a url with the base_url and your api key.
    url = base_url+api_key
    #store the url response as a variable called "response" using the requests library
    response = requests.get(url)
    #The data we get back is a "JSON" file, a very common method of sending data. We need to "translate it" so we can do something with it.
    data = response.json()
    #send the data to the main loop
    return data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key"
#below, paste your NASA API Key.
api_key = "=sYlxxqiOHE2YgKOxQg9xtXZ6b1pFGF458seVL8Zm"
rover_data = fetch_rover(base_url,api_key)
print(rover_data)
#if the response we get back has a 'url', then we probably got a legit response...If not, go to the 'else' below cause somethin dun messed up good
if 'url' in rover_data:
    #Thanks to our data being a JSON, it is easy to sort through and find key words
    #First, find the 'title' in the data and print the data that comes after it
    print("Title:", rover_data['title'])
    #Then, look for date and... well  you probably know the rest...
    print("Date:", rover_data['date'])
    print("Explanation:", rover_data['explanation'])
    print("HD URL:", rover_data.get('hdurl', "Not available"))
    print("URL:", rover_data['url'])

    # Open and display the image
    response = requests.get(rover_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
else:
    print("Error:", rover_data.get('msg', 'Unknown error'))
