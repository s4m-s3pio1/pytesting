#!/usr/bin/python

import hashlib

if __name__ == "__main__":
    hash_val = input("! Enter data to hash: ")

    hash1 = hashlib.md5()
    hash1.update(hash_val.encode())
    print(f"MD5: {hash1.hexdigest()}")

    hash2 = hashlib.sha1()
    hash2.update(hash_val.encode())
    print(f"SHA1: {hash2.hexdigest()}")

    hash3 = hashlib.sha224()
    hash3.update(hash_val.encode())
    print(f"SHA224: {hash3.hexdigest()}")

    hash4 = hashlib.sha256()
    hash4.update(hash_val.encode())
    print(f"SHA256: {hash4.hexdigest()}")

    hash5 = hashlib.sha512()
    hash5.update(hash_val.encode())
    print(f"SHA512: {hash5.hexdigest()}")
