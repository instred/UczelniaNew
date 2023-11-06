import requests, json
from pytesseract import image_to_string
import cv2

def read_image() -> str:


    try:

        image = cv2.imread('image-3.jpg')

    except:
        print("Cannot read image")
        return

    	
    image = image[100:800]

    data = image_to_string(image)

    data = [x.lower() for x in data if x.isalpha()]
    return ''.join(data)

def request_info(country: str) -> dict:


    url = f"https://restcountries.com/v3.1/name/{country}"  # Replace with the actual endpoint URL


    response = requests.get(url)
    json_string = response.text
    data_dict = json.loads(json_string)
    formatted = {'Full name': data_dict[0]['name']['official'], 'Common name': data_dict[0]['name']['common'],
                 'Region': data_dict[0]['region'],
                  'Capital': data_dict[0]["capital"][0], 'Currencies': ', '.join(data_dict[0]['currencies'].keys()),
                'Area': str(data_dict[0]['area']) + " km²", 'Population': str(data_dict[0]['population']) + " people",
                    'Time Zones': ', '.join(data_dict[0]['timezones'])}
    return formatted

if __name__ == "__main__":

    country = read_image()

    info = request_info(country)
    for key in info:
        print(f"{key}: {info[key]}")