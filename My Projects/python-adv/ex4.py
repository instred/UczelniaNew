import qrcode
import cv2
from time import sleep
from validators import url
import webbrowser

def generate_qr() -> None:

    webpage = 'https://longdogechallenge.com/'

    QRCodefile = "image-4.jpg"

    QRimage = qrcode.make(webpage)

    QRimage.save(QRCodefile)

def show() -> None:

    filename = "image-4.jpg"
    image = cv2.imread(filename)

    cv2.imshow('image', image)
    cv2.waitKey(1000)

def decode_qr() -> str:

    filename = "image-4.jpg"
    image = cv2.imread(filename)

    detector = cv2.QRCodeDetector()

    data, vert_array, bin_qr = detector.detectAndDecode(image)

    if vert_array is not None:
        return data
    else:
        print("Error")
        return

if __name__ == '__main__':
    print("Generating QR...")
    generate_qr()
    show()
    print("Decoding QR...")
    sleep(3)
    data = decode_qr()
    print(f"Your QR data: {data}")
    if url(data):
        try:

            user_check = input("Do you want to open this website? [y/n]")
        
        except:
            
            print("Wrong input")
        
        if user_check == 'y':
            webbrowser.open(data)
    
