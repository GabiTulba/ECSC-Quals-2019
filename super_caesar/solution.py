import string

key1 = 9
key2 = 2
ciphertext='YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED'
plaintext=''

for char in ciphertext:
	if char in string.ascii_lowercase:
		plaintext += chr((ord(char) - ord('a') - key1) % 26 + ord('a'))
	else:
		plaintext += chr((ord(char) - ord('A') - key2) % 26 + ord('A'))

print 'ECSC{' + plaintext[plaintext.index('FlAGis') + 6:] + '}'
