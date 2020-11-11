import ecc

SENDER_PRIVATE_KEY = 3
RECEIVER_PRIVATE_KEY = 5

EEC_COMMON_POINT = 7
ELLIPTIC_CURVE = ecc.EC(1, 18, 19)

ORIGINAL_IMAGE = './data/img1.jpg'
SECRET_IMAGE = './data/lena_tiny.png'
OUTPUT_IMAGE = './output/img.png'

INPUT_MESSAGE = input('Enter Message to Hide: ')
