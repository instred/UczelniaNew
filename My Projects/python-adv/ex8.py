import cv2
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import re
from typing import List

def show(image) -> None:
    cv2.imshow('image', image)
    cv2.waitKey(5000)

def read_image() -> str:

    try:

        image = cv2.imread('image-8.jpg')

    except:
        print("Cannot read image")
        return
    
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # _, image = cv2.threshold(image, 200, 150, cv2.THRESH_BINARY)

    data = image_to_string(image)
    # show(image)

    return data


def clean_data(data_string: str) -> dict:
    cleared = {}
    reicept_idx = []
    med = []
    data_split = list(filter(None, data_string.split('\n')))


    for idx, data in enumerate(data_split):
        if "Pacjent" in data:
            cleared["pacient"] = data
        if "Recepta" in data:
            reicept_idx.append(idx)
    for i in reicept_idx:
        med.append(data_split[i+1: i+6])


    for medi in med:
        if "meds" in cleared:
            cleared["meds"].append(med_info(medi))
        else:
            cleared["meds"] = [(med_info(medi))]
    return cleared

def med_info(med: List[str]) -> dict:
    out = {}
    out['Nazwa'] = med[0]
    for data in med:
        if "op." in data:
            out["Zawartosc Paczki"] = data
        if "x" in data:
            out["Dawkowanie"] = data
    return out


def show_data(data: dict) -> None:
    print(data["pacient"])
    print("Przepisane leki: ")
    for med in data["meds"]:
        for m in med:
            print(f"{m}: {med[m]}")
        print(10*"---")

    


if __name__ == "__main__":
    data = read_image()
    cleaned  = clean_data(data)
    show_data(cleaned)