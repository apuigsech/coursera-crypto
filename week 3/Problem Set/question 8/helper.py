#!/usr/bin/env python

# Coursera Crypto I Problem Helper (Problem Set Week 3, Question 8)
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
from cryptohelper import *


def f1(x,y):
	return (strxor(encrypt_block_AES(x, y), y))


def main(argv):
	Z = "deadcafedeadcafedeadcafedeadcafe".decode('hex')

	y1 = "\x00"*16
	y2 = "\x01"*16

	x1 = decrypt_block_AES(strxor(y1, Z), y1)
	x2 = decrypt_block_AES(strxor(y2, Z), y2)

	print x1.encode('hex'),y1.encode('hex'),f1(x1,y1).encode('hex')
	print x2.encode('hex'),y2.encode('hex'),f1(x2,y2).encode('hex')


if __name__ == "__main__":
        main(sys.argv)