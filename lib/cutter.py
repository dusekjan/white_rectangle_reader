import cv2
from PIL import Image


def find_biggest_white(picture_path: str):
    picture = cv2.imread(picture_path)
    
    # Konverze obrázku do odstínů šedi
    grayscale = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    
    # Binarizace - převedení do černobílého obrázku
    _, binarization = cv2.threshold(grayscale, 240, 255, cv2.THRESH_BINARY)

    # Nalezení kontur
    contours, _ = cv2.findContours(binarization, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Nalezení největšího obdélníku
    biggest_rectangle = max(contours, key=cv2.contourArea)
    
    # Získání rozměrů největšího obdélníku
    x, y, width, height = cv2.boundingRect(biggest_rectangle)
    
    # Oříznutí obrazu na základě rozměrů obdélníku
    cut_image = picture[y:y+height, x:x+width]
    print(f"  - ořezáno x:{x} y:{y} w:{width} h:{height}")

    # Uložení oříznutého obrazu
    # cv2.imwrite('./obrazku.jpg', cut_image)

    # pouzit stejny format jako knihovna PIL
    rgb_cut_image = cv2.cvtColor(cut_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb_cut_image)
