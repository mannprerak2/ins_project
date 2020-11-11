import random
from ecc import EC
from stegano import lsb
from utils import *
from hill_cipher import *
import config
import lsb


class Prog:
    lsbobj = lsb.LSB()

    def keyGenerator(self):
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

    def encryptImage(self, keyMatrix: list, inputImage):
        # text = input("Enter the data to be encrypted: ")
        text = config.INPUT_MESSAGE
        cipher_text = hill_encryption(text, keyMatrix)

        print("Encrypted data is: ", cipher_text)

        secret_image = self.lsbobj.encode_image(
            inputImage, cipher_text)

        print("Hid cipher text in image successfuly")
        return secret_image

    def decryptImage(self, keyMatrix: list, inputImage):
        recovered_text = self.lsbobj.decode_image(inputImage)
        print("Text recovered from image:", recovered_text)

        decrypted_text = hill_decryption(recovered_text, keyMatrix)
        return decrypted_text


prog = Prog()

k = prog.keyGenerator()

prog.encryptImage(k, config.ORIGINAL_IMAGE).save(config.OUTPUT_IMAGE)
print('Decrypted ciphertext:', prog.decryptImage(k, config.OUTPUT_IMAGE))
