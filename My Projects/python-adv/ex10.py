import cv2
from pytesseract import image_to_string
from typing import List
import matplotlib.pyplot as plt

def show() -> None:

    image = cv2.imread('image-10.jpg')
    cv2.imshow('image', image)
    cv2.waitKey(1500)

def read_image() -> List[str]:

    try:

        image = cv2.imread('image-10.jpg')

    except:
        print("Cannot read image")
        return
    
    image = image[70:1100]

    data = image_to_string(image)

    animals = []
    cleared = list(filter(None, data.split('\n')))
    animals_lines = [line.split(" ") for line in cleared if len(line)>13]
    animals_lines[0][0] = animals_lines[0][0].upper()

    # all animals are in uppercase so we can easily extract them from string

    for line in animals_lines:
        for animal in line:
            if animal.isupper():
                animals.append(animal)

    return animals

def match_animal(animal: str) -> str:
    mammals = ["RABBIT", "SHEEP", "ELEPHANT", "CAT", "KANGAROO", "DOG", "HIPPOPOTAMUS", "HORSE", "PIG", "COW"]
    fish = ["SALMON", "TUNA", "GOLDFISH", "CLOWNFISH", "ANGELFISH", "SWORDFISH", "SHARK", "TROUT", "CATFISH", "PIRANHA", "FISH"]
    birds = ["EAGLE", "HEN", "PENGUIN", "OSTRICH", "FLAMINGO", "HAWK", "PARROT", "PEACOCK", "OWL", "HUMMINGBIRD"]
    reptiles = ["SNAKE", "TURTLE", "CROCODILE", "IGUANA", "GECKO", "CHAMELEON", "LIZARD", "TORTOISE", "KOMODO DRAGON", "ALLIGATOR"]

    match animal:
        case item if item in mammals:
            return "mammals"
        case item if item in fish:
            return "fish"
        case item if item in birds:
            return "birds"
        case item if item in reptiles:
            return "reptiles"
        case _:
            print(animal)
            return

def plot_bar(classes: dict) -> None:
    values = list(classes.values())
    animal_class = list(classes.keys())
    print(animal_class, values)

    plt.bar(animal_class, values)

    plt.title("Animal Classess with their number")

    plt.show()


if __name__ == "__main__":
    
    classes_count = {}
    # show()
    image_data = read_image()
    for animal in image_data:
        matching = match_animal(animal)
        if matching in classes_count:
            classes_count[matching] += 1
        else:
            classes_count[matching] = 1
        
    plot_bar(classes_count)
