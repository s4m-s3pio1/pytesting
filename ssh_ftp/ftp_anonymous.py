#!/usr/bin/python

import ftplib


def ftp_login(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login("anonymous", "anonymous")
        print(f"<> {host} anonymous login successful")
        ftp.quit()
        return True
    except Exception:
        print(f"<> {host} anonymous login failed")


if __name__ == "__main__":
    host = input("! Enter IP/hostname: ")
    ftp_login(host)
