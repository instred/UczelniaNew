from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import numpy as np

def simple() -> None:
    img = Image.open("testocr.png")

    text = pytesseract.image_to_string(img)
    print(text)

    with open("tekst.txt", "w") as f:

        f.write(text)


def advanced() -> None:
    img = Image.open("15.png")
    text = pytesseract.image_to_string(img)
    print(text)

    try:

        x = float(text)

    except ValueError:

        print("Nie udało się przekonwertować tekstu na liczbę")
        exit()


    x_values = np.linspace(0, 2*np.pi, 100)


    y_values = np.sin(x*x_values)


    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title(f"Wykres funkcji sin({x}x)")
    plt.savefig('wykres.png')
    plt.show()
    



if __name__ == '__main__':
    advanced()
