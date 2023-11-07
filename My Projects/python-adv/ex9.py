import cv2
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import re

def show() -> None:

    image = cv2.imread('image-9.jpg')
    cv2.imshow('image', image)
    cv2.waitKey(1500)

def read_image() -> str:

    try:

        image = cv2.imread('image-9.jpg')

    except:
        print("Cannot read image")
        return
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 200, 150, cv2.THRESH_BINARY)
    

    data = image_to_string(image)
    
    return data


def clean_data(data_string: str) -> dict:
    cleared = {}
    data_split = list(filter(None, data_string.split('\n')))
    data_split = data_split[1:-1]
    for product in data_split:
        price = product[-4:]
        parts = re.split(r'[^a-zA-Z]+', product[1:])
        product_name = product[0] + ' '.join([x for x in parts if x ])
        cleared[product_name] = price


    return cleared


def show_products(data: dict) -> None:

    print("Products list:")
    for product in data:
        print(f"{product}: ${data[product]}")

def plot_diagram(data: dict) -> None:

    labels = data.keys()
    sizes = data.values()

    plt.figure(figsize=(12, 9))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    plt.title("Products as a chart")

    plt.show()

if __name__ == "__main__":
    print("Showing your shopping list...")
    print("We will consider products only from CharMar")
    # show()
    image_data = read_image()
    cleared_data = clean_data(image_data)
    show_products(cleared_data)
    plot_diagram(cleared_data)
