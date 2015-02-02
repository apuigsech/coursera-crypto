#!/usr/bin/env python

# Coursera Crypto I Problem Helper (Problem Set Week 4, Question 1)
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

import random
import sys
from cryptohelper import *

iv = ''.join([chr(random.randint(0,255)) for i in range(16)])
key = ''.join([chr(random.randint(0,255)) for i in range(16)])
pt = 'Pay Bob 100$'

ct = '20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d'.decode('hex')

# Stupid hack to change one byte in string.
def str_set_chr(s, idx, value):
	s = list(s)
	s[idx] = value
	return ''.join(s)


def test():
	global iv
	ct = encrypt_block_CBC(pt, 16, iv, key, encrypt_block_AES)
	iv = str_set_chr(iv, 8, chr(ord(iv[8])^ord('1')^ord('5')))
	npt = decrypt_block_CBC(ct, 16, iv, key, decrypt_block_AES)
	print npt


def main(argv):
	global ct
	print ct.encode('hex')
	ct = str_set_chr(ct, 8, chr(ord(ct[8])^ord('1')^ord('5')))
	print ct.encode('hex')


if __name__ == "__main__":
        main(sys.argv)