from pwn import *
s1=remote('37.128.230.46','50021')
s2=remote('37.128.230.46','50021')
print s1.recvline()
s1.sendline('gabi')
print s2.recvline()
s2.sendline('gabi')
print s1.recvline()
print s2.recvline()
s1.sendline('123')
x=s1.recvline().strip()[56:].split()[0]
print x
s2.sendline(x)
print s2.recvline().strip()
print s2.recvline().strip()
