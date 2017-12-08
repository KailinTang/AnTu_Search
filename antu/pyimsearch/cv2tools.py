import cv2

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


def find_im(d):
    img = cv2.imread(str(d))

    return img


def find_string(img):
    s = pytesseract.image_to_string(img)
    print(s,'aaaaa')
    return s
