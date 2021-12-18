from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def encrypt_password(password):
    return PasswordHasher().hash(password)


def verify_password(password, hash):
    try:
        return PasswordHasher().verify(hash, password)
    except VerifyMismatchError:
        return False
