import dct
import json
import config
import random
import stegano
from ecc import EC
from utils import *
from stegano import lsb
from hill_cipher import *


def generateKey():
    """Returns a self invertible matrix key."""
    ec = config.ELLIPTIC_CURVE
    o, _ = ec.at(config.EEC_COMMON_POINT)

    print("Common point selected is ({}, {})\n".format(o.x, o.y))

    # a -> sender, b -> receiver
    pvt_a = config.SENDER_PRIVATE_KEY
    pub_a = ec.mul(o, pvt_a)
    print("Public key of sender is ({}, {})\n".format(pub_a.x, pub_a.y))

    pvt_b = config.RECEIVER_PRIVATE_KEY
    pub_b = ec.mul(o, pvt_b)
    print("Public key of receiver is ({}, {})\n".format(pub_b.x, pub_b.y))

    # Encryption
    # Sender encrypts data before sending

    # pub_b = o * pvt_b
    # K = o * (pvt_b + pvt_a)

    # pvt_b, o, pub_a
    # K = pub_a * pvt_b
    # K = o * (pvt_a + pvt_b)

    K = ec.mul(pub_b, pvt_a)
    x, y = K.x, K.y

    K1 = ec.mul(o, x)
    K2 = ec.mul(o, y)

    # Key
    Km = [[K1.x, K1.y], [K2.x, K2.y]]
    print("Key is: ")
    printMatrix(Km)

    N = 3
    a, b, c, d = Km[0][0], Km[0][1], Km[1][0], Km[1][1]

    # Self invertible key matrix
    k = []

    k.append([
        a,
        b,
        (N * (1 - a)) % 94,
        (N * (0 - b)) % 94,
    ])

    k.append([
        c,
        d,
        (N * (0 - c)) % 94,
        (N * (1 - d) % 94)
    ])

    k.append([
        moddiv(1 + a, N, 94),
        moddiv(b, N, 94),
        (-a) % 94,
        (-b) % 94,
    ])
    k.append([
        moddiv(c, N, 94),
        moddiv(1 + d, N, 94),
        (-c) % 94,
        (-d) % 94,
    ])

    print("Self invertible matrix key is: ")
    printMatrix(k)
    return k


# Generate matrix key for Hill Cipher using EEC
k = generateKey()

# Encrypt the message using Hill Cipher
encrypted_text = hill_encryption(config.INPUT_MESSAGE, k)


# Get DCT coeffs for the secret image
dct_coeffs = dct.get_dct_coeffs(config.SECRET_IMAGE)
print('Extracted DCT coeffs:', len(dct_coeffs), 'x', len(dct_coeffs[0]))

# Serialise the object containing payload
encoded = json.dumps({'dct': dct_coeffs, 'cipher': encrypted_text})

# Save the encoded information to the image
stegano.lsb.hide(config.ORIGINAL_IMAGE, encoded).save(config.OUTPUT_IMAGE)
print("Saved information to image:", config.OUTPUT_IMAGE)

# Pause before decryption begins
input("\nHit enter to start decryption:")

# Recover text from saved image
recovered_text = stegano.lsb.reveal(config.OUTPUT_IMAGE)

data = json.loads(recovered_text)

# Recover data from the serialised string
ciphertext = data['cipher']
recovered_coeffs = data['dct']

# Decrypt text using Hill Cipher
decrypted_text = hill_decryption(ciphertext, k)
print("Decrypted text:", decrypted_text)

# Regenerate saved image using recovered coefficients
dct.regenerate_images(recovered_coeffs, config.RECOVERED_IMAGE)
print("Recovered image:", config.RECOVERED_IMAGE)
