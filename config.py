import ecc

SENDER_PRIVATE_KEY = 3
RECEIVER_PRIVATE_KEY = 5

EEC_COMMON_POINT = 7
ELLIPTIC_CURVE = ecc.EC(1, 18, 19)

ORIGINAL_IMAGE = './data/img1.jpg'
DCT_IMAGE = './data/img_dct.png'
ENCRYPTED_IMAGE = './data/img_enc.png'
OUTPUT_IMAGE = './output/img.png'

INPUT_MESSAGE = input('Enter Message to Hide: ')
