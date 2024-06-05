# Day 4 - Part 1

import hashlib


def calculateSecretDecimal(secret):
    key_loop = 1
    while True:
        hash = hashlib.md5(f"{secret}{key_loop}".encode("utf-8")).hexdigest()
        if hash.startswith("00000"):
            break
        key_loop += 1

    return key_loop


if __name__ == "__main__":
    secret = "yzbqklnj"
    print(calculateSecretDecimal(secret))
