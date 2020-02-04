#!/usr/bin/env python3

import getpass
import telnetlib

HOST = "99.99.99.1"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"!HELLO WORLD!\n")
#tn.write(b"enable\n")
#tn.write(b"cisco\n")
#tn.write(b"conf t\n")
#tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
