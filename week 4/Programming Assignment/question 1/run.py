#!/usr/bin/env python

# Coursera Crypto I Problem Solution (Week 4, Question 1)
#
# Copyright (c) 2015 - Albert Puigsech Galicia (albert@puigsech.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys
import urllib2
from cryptohelper import *
import sys


ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')
charset=''.join([chr(i) for i in range(0,256)])

TARGET = 'http://crypto-class.appspot.com/po?er='


# Stupid hack to change one byte in string.
def str_set_chr(s, idx, value):
	s = list(s)
	s[idx] = value
	return ''.join(s)


def padding_oracle_request(ct):
	url = TARGET + ct.encode('hex')
	req = urllib2.Request(url)
	try:
		f = urllib2.urlopen(url)
	except urllib2.HTTPError, e:
		if e.code != 404:
			return False
	return True


def padding_oracle(ct, charset):
	guess_pt = ''
	iv = ct[:16]
	ct = ct[16:]
	ct_blocks = block_split(ct)

	for i in range(-1, len(ct_blocks)-1):
			if i >= 0:
				target = ct_blocks[i]
			else:
				target = iv
			guess_block = "\x00"*16
			for j in range(1,len(target)+1):
				padding = "\x00"*(16-j)+chr(j)*j
				for ch in charset:
					if ch == '\x01' and i == len(ct_blocks)-2:
						continue
					guess_block = str_set_chr(guess_block, 16-j, ch)
					new_target = strxor(target, strxor(guess_block, padding))
					if i >= 0:
						ct_blocks[i] = new_target
					else:
						iv = new_target
					sys.stdout.write("TRY %s [%s] => [%s]\r" % ((iv + block_join(ct_blocks[:i+2])).encode('hex'), guess_block.encode('hex'), guess_pt.encode('hex')))
					sys.stdout.flush()
					if padding_oracle_request(iv + block_join(ct_blocks[:i+2])) == True:
						break
			guess_pt += guess_block
	return guess_pt 

def main(argv):
	pt = padding_oracle(ct, charset)
	print "Decrypted:", pt

if __name__ == "__main__":
        main(sys.argv)
