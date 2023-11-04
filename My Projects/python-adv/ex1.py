from pytesseract import image_to_string
import matplotlib.pyplot as plt
import cv2





def read_graph() -> None:


    try:

        image = cv2.imread('graph.jpg')

    except:
        print("Cannot read image")
        return

    data = image_to_string(image)
    x_cord = range(-50, 50)
    y_cord = [abs(x) for x in x_cord]
    funx = data[:9]

    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    plt.title(funx)
    plt.plot(x_cord, y_cord)
    plt.show()

if __name__ == '__main__':
    read_graph()