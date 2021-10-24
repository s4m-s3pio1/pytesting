#!/usr/bin/python

import hashlib

if __name__ == "__main__":
    md5_hash = input("! Enter MD5 hash: ")
    pwd_list = input("! Enter password list path: ")
    try:
        file = open(pwd_list, "r")
    except:
        print("!! File not found.")
        quit()
    for pwd in file:
        pwd = pwd.strip("\n")
        pwd_enc = pwd.encode("utf-8")
        md5_dig = hashlib.md5(pwd_enc).hexdigest()
        if md5_dig == md5_hash:
            print(f"Password found: {pwd}")
            exit(0)
