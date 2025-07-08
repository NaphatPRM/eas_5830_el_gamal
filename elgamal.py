import random

from params import p
from params import g

def keygen():
    q = (p - 1) / 2
    sk = random.randint(1, q)
    pk = pow(g, sk, p)
    return pk,sk


def encrypt(pk,m):
    q = (p - 1) / 2
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * m) % p
    return [c1,c2]


def decrypt(sk,c):
    first = pow(c[0], sk, p)
    val_below = modular_inverse(first, p)
    m = (c[1] * val_below) % p
    return m


def modular_inverse(a, m):
    """
    Calculates the modular inverse of 'a' modulo 'm'.
    There is no need to update this function.
    """
    return pow(a, -1, m)

