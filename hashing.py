import hashlib
from argon2 import PasswordHasher

ph = PasswordHasher()  # Initiate hash object
def argon_hash(password):
    hash = ph.hash(f"{password}")
    return hash
