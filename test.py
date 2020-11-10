
# Base Image
baseImg = './data/img1.jpg'
# Secret Image
secretImg = './data/img2.jpg'

"""
Encryption Steps -
1. Hide secret image inside Base image to generate Out1 image.
2. Convert PlainText to Ciphertext using ECC and Hill Cipher.
3. Hide Ciphertext to Out1 image to generate Output image.

Decryption Steps -
1. Extract ciphertext from Input Image.
2. Extract secret image from Input Image.
"""
