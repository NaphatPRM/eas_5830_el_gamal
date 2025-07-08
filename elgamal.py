import random

from params import p
from params import g

def keygen():
    q = (p - 1) / 2
    sk = random.randint(1, q)
    pk = (g ** sk) % p
    return pk,sk


def encrypt(pk,m):
    q = (p - 1) / 2
    r = random.randint(1, q)
    c1 = (g ** r) % p
    c2 = ((pk ** r) * m) % p
    return [c1,c2]


def decrypt(sk,c):
    val_below = modular_inverse(c[0] ** sk, -1, p)
    m = (c[1] * val_below) % p
    return m


def modular_inverse(a, m):
    """
    Calculates the modular inverse of 'a' modulo 'm'.
    There is no need to update this function.
    """
    return pow(a, -1, m)

