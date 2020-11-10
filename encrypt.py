import random
from ecc import EC
from stegano import lsb
from utils import *
from hill_cipher import *


ec = EC(1, 18, 19)

# Selecting a common point for both
o, _ = ec.at(7)
print("Common point selected is ({}, {})\n".format(o.x, o.y))

# a -> sender, b -> receiver
pvt_a = int(input("Enter sender's private key: "))
pub_a = ec.mul(o, pvt_a)
print("Public key of sender is ({}, {})\n".format(pub_a.x, pub_a.y))

pvt_b = int(input("Enter receiver's private key: "))
pub_b = ec.mul(o, pvt_b)
print("Public key of receiver is ({}, {})\n".format(pub_b.x, pub_b.y))

# Encryption
# Sender encrypts data before sending

K = ec.mul(pub_a, pvt_a)
x, y = K.x, K.y

K1 = ec.mul(o, x)
K2 = ec.mul(o, y)

# Key
Km = [[K1.x, K1.y], [K2.x, K2.y]]
print("Key is: ")
printMatrix(Km)

# N = random.randrange(10) + 3
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

text = input("Enter the data to be encrypted: ")
cipher_text = hill_encryption(text, k)

print("Encrypted data is: ", cipher_text)

secret_image = lsb.hide("./data/img.png", cipher_text)
secret_image.save("./output/img.png")

print("Hid cipher text in image successfuly")
