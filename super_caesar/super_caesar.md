# super_caesar (250 points / 53 solves)
## Problem statement:

>Alice finally realized that Caesar’s cipher is insecure, so she decided to switch to something stronger: a modified version of Caesar’s cipher that uses two keys. <br>
>You intercepted the following message: <br>
>Code: <br>
>bcjac --- YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED --- UVQR <br>
>Decrypt and find your flag. <br>

## My opinion:

This problem was a simple Caesar Cipher problem it was the only crypto challenge that I actually enjoyed solving. <br><br>

## The problem:

so we are given a code that has lowercase and uppercase letters. firstly I tried to apply a Caesar Shift with bruteforce and I saw that with `key 9` I got the first part (which was all lowercase) to decrypt to `start` and the last part (which was all uppercase) to decrypt to `STOP`. So I concluded that the uppercase letters were encrypted with a key and the lowercase with another key. That gave us the flag. 

## The code:

The following code is the key finder described above: <br>
```python
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
```
<br><br>
and it prints the following:
```
Key: 0 plaintext: bcjac --- YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED --- UVQR
Key: 1 plaintext: abizb --- XmtMlPOFgPVpBWFTwtWmEUpqTUBTLgPczGtBHqaCHbTpmJwaONQXSyUBCAklZpsJmDIboDC --- TUPQ
Key: 2 plaintext: zahya --- WlsLkONEfOUoAVESvsVlDTopSTASKfObyFsAGpzBGaSolIvzNMPWRxTABZjkYorIlCHanCB --- STOP
Key: 3 plaintext: yzgxz --- VkrKjNMDeNTnZUDRurUkCSnoRSZRJeNaxErZFoyAFzRnkHuyMLOVQwSZAYijXnqHkBGzmBA --- RSNO
Key: 4 plaintext: xyfwy --- UjqJiMLCdMSmYTCQtqTjBRmnQRYQIdMzwDqYEnxZEyQmjGtxLKNUPvRYZXhiWmpGjAFylAZ --- QRMN
Key: 5 plaintext: wxevx --- TipIhLKBcLRlXSBPspSiAQlmPQXPHcLyvCpXDmwYDxPliFswKJMTOuQXYWghVloFiZExkZY --- PQLM
Key: 6 plaintext: vwduw --- ShoHgKJAbKQkWRAOroRhZPklOPWOGbKxuBoWClvXCwOkhErvJILSNtPWXVfgUknEhYDwjYX --- OPKL
Key: 7 plaintext: uvctv --- RgnGfJIZaJPjVQZNqnQgYOjkNOVNFaJwtAnVBkuWBvNjgDquIHKRMsOVWUefTjmDgXCviXW --- NOJK
Key: 8 plaintext: tubsu --- QfmFeIHYzIOiUPYMpmPfXNijMNUMEzIvsZmUAjtVAuMifCptHGJQLrNUVTdeSilCfWBuhWV --- MNIJ
Key: 9 plaintext: start --- PelEdHGXyHNhTOXLolOeWMhiLMTLDyHurYlTZisUZtLheBosGFIPKqMTUScdRhkBeVAtgVU --- LMHI
Key: 10 plaintext: rszqs --- OdkDcGFWxGMgSNWKnkNdVLghKLSKCxGtqXkSYhrTYsKgdAnrFEHOJpLSTRbcQgjAdUZsfUT --- KLGH
Key: 11 plaintext: qrypr --- NcjCbFEVwFLfRMVJmjMcUKfgJKRJBwFspWjRXgqSXrJfcZmqEDGNIoKRSQabPfiZcTYreTS --- JKFG
Key: 12 plaintext: pqxoq --- MbiBaEDUvEKeQLUIliLbTJefIJQIAvEroViQWfpRWqIebYlpDCFMHnJQRPzaOehYbSXqdSR --- IJEF
Key: 13 plaintext: opwnp --- LahAzDCTuDJdPKTHkhKaSIdeHIPHZuDqnUhPVeoQVpHdaXkoCBELGmIPQOyzNdgXaRWpcRQ --- HIDE
Key: 14 plaintext: novmo --- KzgZyCBStCIcOJSGjgJzRHcdGHOGYtCpmTgOUdnPUoGczWjnBADKFlHOPNxyMcfWzQVobQP --- GHCD
Key: 15 plaintext: mnuln --- JyfYxBARsBHbNIRFifIyQGbcFGNFXsBolSfNTcmOTnFbyVimAZCJEkGNOMwxLbeVyPUnaPO --- FGBC
Key: 16 plaintext: lmtkm --- IxeXwAZQrAGaMHQEheHxPFabEFMEWrAnkReMSblNSmEaxUhlZYBIDjFMNLvwKadUxOTmzON --- EFAB
Key: 17 plaintext: klsjl --- HwdWvZYPqZFzLGPDgdGwOEzaDELDVqZmjQdLRakMRlDzwTgkYXAHCiELMKuvJzcTwNSlyNM --- DEZA
Key: 18 plaintext: jkrik --- GvcVuYXOpYEyKFOCfcFvNDyzCDKCUpYliPcKQzjLQkCyvSfjXWZGBhDKLJtuIybSvMRkxML --- CDYZ
Key: 19 plaintext: ijqhj --- FubUtXWNoXDxJENBebEuMCxyBCJBToXkhObJPyiKPjBxuReiWVYFAgCJKIstHxaRuLQjwLK --- BCXY
Key: 20 plaintext: hipgi --- EtaTsWVMnWCwIDMAdaDtLBwxABIASnWjgNaIOxhJOiAwtQdhVUXEZfBIJHrsGwzQtKPivKJ --- ABWX
Key: 21 plaintext: ghofh --- DszSrVULmVBvHCLZczCsKAvwZAHZRmVifMzHNwgINhZvsPcgUTWDYeAHIGqrFvyPsJOhuJI --- ZAVW
Key: 22 plaintext: fgneg --- CryRqUTKlUAuGBKYbyBrJZuvYZGYQlUheLyGMvfHMgYurObfTSVCXdZGHFpqEuxOrINgtIH --- YZUV
Key: 23 plaintext: efmdf --- BqxQpTSJkTZtFAJXaxAqIYtuXYFXPkTgdKxFLueGLfXtqNaeSRUBWcYFGEopDtwNqHMfsHG --- XYTU
Key: 24 plaintext: delce --- ApwPoSRIjSYsEZIWzwZpHXstWXEWOjSfcJwEKtdFKeWspMzdRQTAVbXEFDnoCsvMpGLerGF --- WXST
Key: 25 plaintext: cdkbd --- ZovOnRQHiRXrDYHVyvYoGWrsVWDVNiRebIvDJscEJdVroLycQPSZUaWDECmnBruLoFKdqFE --- VWRS
```
<br><br>
The following code is the decryptor:
```python
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
```
<br><br>
Flag: **ECSC{BGtSheIosNMPWRqTABZcdYhkIeCHtgCB}**
