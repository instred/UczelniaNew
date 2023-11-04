from pytesseract import image_to_string
import matplotlib.pyplot as plt
import cv2
from re import match


def validate(s : str) -> bool:
    ver1 = '^[A-Z]{2} [A-Z0-9]{4,5}$'
    ver2 = '^[A-Z]{3} [A-Z0-9]{4,5}$'
    return bool(match(ver1, s)) or bool(match(ver2, s))



def read_table() -> str:

    try:

        image = cv2.imread('regis-table.jpg')

    except:
        print("Cannot read image")
        return

    	
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # wycinam tylko potrzebne czesci zdjecia
    roi = gray[300:600, 70:800]

    text = image_to_string(roi)

    # wycinam znaki nowej linii
    text = text[:-2]
    return text





if __name__ == "__main__":
    if validate(read_table()):
        print("Tablica Poprawna")
    else:
        print("Tablica Niepoprawna")