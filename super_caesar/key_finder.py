enc_flag = 'bcjac --- YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED --- UVQR'

def is_lower(char):
	return ord(char) >= ord('a') and ord(char) <= ord('z')

def is_upper(char):
	return ord(char) >= ord('A') and ord(char) <= ord('Z')

for key in range(26):
	shifted = ''
	for char in enc_flag:
		if is_lower(char):
			char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
		elif is_upper(char):
			char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
		shifted += char
	print 'Key:', key, 'plaintext:', shifted	
