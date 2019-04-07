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
