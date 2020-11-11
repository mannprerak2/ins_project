import ecc

SENDER_PRIVATE_KEY = 3
RECEIVER_PRIVATE_KEY = 5

EEC_COMMON_POINT = 7
ELLIPTIC_CURVE = ecc.EC(1, 18, 19)

ORIGINAL_IMAGE = './data/base.jpg'
SECRET_IMAGE = './data/secret.png'
OUTPUT_IMAGE = './output/stego.png'
RECOVERED_IMAGE = './output/secret.png'

INPUT_MESSAGE = input('Enter Message to Hide: ')
