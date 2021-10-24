#!/usr/bin/python

from urllib.request import urlopen
import hashlib


if __name__ == "__main__":
    sha1_hash = input("! Enter SHA1 hash: ")
    pwd_list = str(
        urlopen(
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
        ).read(),
        "utf-8",
    )
    for pwd in pwd_list.split("\n"):
        hash_predict = hashlib.sha1(bytes(pwd, "utf-8")).hexdigest()
        if hash_predict == sha1_hash:
            print(f"<> Password found: {pwd}")
            break
    else:
        print("!! Password not found")
