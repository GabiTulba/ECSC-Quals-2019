# Crypto Luck (150 points / 47 solves)
## Problem statement:

>Test your luck here: 37.128.230.46:50041

## My opinion:

So this problem was actually very similar to the Captcha proof of work used during some bigger CTFs, but was actually simpler than that, not really a crypto challenge to be honest. <br><br>

## The problem:

We were given the following script that was running on a server: <br>
```python
from __future__ import print_function
import string
import random
import hashlib


import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# this function will return the flag.
def flag():
    print("ECSC{the flag is on the server ;)}"+"\n")

def random_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


count = 0
while True:
    token = "ECSC" + random_generator(50)
    eprint("Generated token: " + token + "\r\n")
    sha1 = hashlib.sha1(token.encode())
    sha1 = sha1.hexdigest()[0:6]
    print(sha1)
    data = raw_input("Your token is:")
    eprint("Read from client: " + data + "\r\n")
    if not data: break
    check = hashlib.sha1(data.rstrip("\n\r").encode())
    check = check.hexdigest()[0:6]
    if sha1 == check:
        count = count + 1
        eprint(count)
        if (count >= 10):
            flag()
            break
        

print('EXIT!')

exit()
```
<br><br>
So basically, we need to find 10 times a string with a hexdigest starting with some specific 6 character preffix. My approach to solving this challenge was a birthday attack, since I didn't have to guess 10 hashes in a row, but 10 in total. I precalculated a dictionary with a couple million hashes and the read queries from the server, if the preffix was in my dictionary I would answer, otherwise I would skip the query. The total preffix search space is 3 bytes = 256^3 or 16777216 possible preffixes. The probability to get a preffix in my dictionary would be my dictionary space over the search space (about 1/8). So in about 80 queries I would get 10 hashes that are exist in my dictionary and get the flag. <br><br> 
## The code:

The following code is the exploit described above: <br>
```python
import string
import random
import socket
from hashlib import sha1

def get_random_string(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

dictionary={}
for i in range(2 * 10**6):
	if i % 100000 == 0:
		print 'generated', i, 'random strings!'
	rand_str = get_random_string()
	dictionary[sha1(rand_str).hexdigest()[:6]] = rand_str

print 'total dictionary space:', len(dictionary)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
s.connect(('37.128.230.46', 50041))

correct_answers = 0
while correct_answers<10:
	preffix = s.recv(6)
	s.recv(2) #read newline bytes
	if not preffix in dictionary:
		s.sendall('junk\n')
		continue
	correct_answers += 1
	s.sendall(dictionary[preffix] + '\n')

print s.recv(1024)
```

<br><br>
Flag: **ECSC{bab4d1bdea5baf2a5ce69c2fd7e4945edd39970bc0eb49ea390d58a7d24c3986}**

