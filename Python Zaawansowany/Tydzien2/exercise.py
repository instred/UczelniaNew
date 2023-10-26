from cv2 import imread, cvtColor, COLOR_BGR2RGB
from pytesseract import image_to_string
from collections import namedtuple
from typing import List

# Program do czytania konkretnego schematu faktury

# Wykorzystuje tesseract i opencv

# funkcja pomocniczna do zapisu w pliku

def write_to_file(text: List[str] | str, title=False) -> None:
    with open("invoice.txt", "a") as f:
        if title:
            f.write(text + '\n')
        else: 
            for line in text:
                f.write(line + '\n')



def read_invoice() -> None:

    # Wczytuje obraz uzywajac cv2

    image = imread("invoice.png")

    # tworze sobie tablice krotek w ktorej znajduja sie prostokaty z ktorych program ma czytac 
    # moge w ten sposob uporzadkowac dane z konkretnych miejsc

    OCRLocation = namedtuple("OCRLocation", ["id", "box"])

    OCR_LOCATIONS = [
        OCRLocation("your_company", (530, 60, 770, 190),),

        OCRLocation("billed_to", (60, 270, 400, 150),),

        OCRLocation("dates_and_data", (440, 250, 800, 150),),

        OCRLocation("items_list", (60, 460, 800, 260),),

        OCRLocation("costs", (60, 720, 800,200),),

        OCRLocation("additional", (60, 920, 800,80),)]

    print("OCR'ing document...")
    
    parsingResults = []

    # petla for przelatuje przez lokalizacje prostokatow

    for loc in OCR_LOCATIONS:

        # tworze nasze ROI przy pomocy wspolrzednych
        (x, y, w, h) = loc.box
        roi = image[y:y+h, x:x + w]

        # nastepnie czytam z naszego prostokata dane

        rgb = cvtColor(roi, COLOR_BGR2RGB)
        text = image_to_string(rgb)

        # przeczytane dane splituje i zapisuje do listy

        for line in text.split("\n"):

            if len(line) == 0:
                continue

            parsingResults.append((loc, line))

    # tworze slownik gdzie kluczem bedzie kazdy prostokat a wartosciami list z danymi z konkretnego obszaru

    data = {"your_company": [], "billed_to": [], "dates_and_data": [], "items_list": [], "costs": [], "additional": []}

    for x in parsingResults:

        data[x[0][0]].append(x[1])

    # na koniec zapisuje wszystko do pliku
    # oczywiscie dane w pliku mozna odpowiednio uporzadkowac przed zapisem, ale skoro mamy wszystko pod reka w slowniku nie widzialem potrzeby porzadkowania w pliku .txt

    for key in data:
        write_to_file(f"[{key}]", title=True)
        write_to_file(data[key])
        

if __name__ == '__main__':

    read_invoice()