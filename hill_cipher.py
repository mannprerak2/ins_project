import numpy as np
from numpy.linalg import inv
import utils
# Hill Cipher encryption-decryption using a self invertible matrix of 4x4 dim.


def __split2len(s, n):
    """Split string s to chunks of size n."""
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))


__mod = 94


def __char2Val(s):
    """Convert char s to ASCII value - 32."""
    return ord(s) - 32


def __val2Char(n):
    """Convert int value +32 to ASCII."""
    return chr(n+32)


def hill_encryption(message: str, mat: list):
    assert len(mat) == 4 and len(mat[0]) == 4, "Key Matrix must be of 4x4 dim."
    messageInChunks = __split2len(message, 4)
    cipherText = ""
    for plaintextChunk in messageInChunks:
        for i in range(4):
            val = 0
            for j in range(len(plaintextChunk)):
                val += mat[i][j]*__char2Val(plaintextChunk[j])
            val = val % __mod
            cipherText += __val2Char(val)
    return cipherText


def hill_decryption(ciphertext: str, mat: list):
    assert len(mat) == 4 and len(mat[0]) == 4, "Key Matrix must be of 4x4 dim."
    return hill_encryption(ciphertext, mat)


if __name__ == '__main__':
    # mat = [
    #     [15, 11, 1, 18],
    #     [48, 78, 0, 8],
    #     [1, 1, 0, 1],
    #     [79, 83, 93, 76]
    # ]
    mat = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    utils.printMatrix(mat)
    utils.printMatrix(inv(mat))
    message = "plaintext message"
    print(message)
    ciphertext = hill_encryption(message, mat)
    print(ciphertext)
    plaintext = hill_decryption(ciphertext, mat)
    print(plaintext)
