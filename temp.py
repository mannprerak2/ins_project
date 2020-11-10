import random
from utils import *

# N = random.randrange(10) + 3
N = 3
[a, b, c, d] = [3, 6, 5, 2]

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
