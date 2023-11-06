from pytesseract import image_to_string
import cv2
import re


def show() -> None:

    filename = "image-5.jpg"
    image = cv2.imread(filename)
    image = image[40:]

    cv2.imshow('image', image)
    cv2.waitKey(3000)


def rmv_chars(string: str) -> str | None:

    regex = re.compile('[a-zA-Z]')
    string = ''.join([i for i in string if i.isalnum() or i == ' '])

    search = re.search(regex, string)
    return string if search else None 


def read_image() -> str:


    try:

        image = cv2.imread('image-5.jpg')

    except:
        print("Cannot read image")
        return


    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 205, 255, cv2.THRESH_BINARY)

    data = image_to_string(image)

    lines = data.split('\n')
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    url = non_empty_lines[0]
    coords, _ = url.split("@")[1].split("z")
    lat, long, _ = coords.split(',')
    result = {'Map Coordinates': f"{lat} {long}", "Towns": ""}

    towns = non_empty_lines[3:]
    cleared_towns = []

    for string in towns:
        new_s = rmv_chars(string)
        if new_s is not None:
            cleared_towns.append(new_s)

    result['Towns'] = ', '.join(cleared_towns)  
    return result

if __name__ == '__main__':
    result = read_image()
    for key in result:
        print(f"{key}: {result[key]}")
    show()
