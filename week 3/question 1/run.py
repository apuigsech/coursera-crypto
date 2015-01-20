#!/usr/bin/env python

# Coursera Crypto I Problem Solution (Week 3, Question 1)
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
import hashlib
from cryptohelper import *


def calc_digest(data):
	chunks = block_split(data, 1024)

	for i in range(len(chunks)-1, 0, -1):
        	chunks[i-1] = chunks[i-1] + hashlib.sha256(chunks[i]).digest()

	return hashlib.sha256(chunks[0])


def main(argv):
	if len(argv) < 2:
		print "Usage:\n\trun.py <filename>\n"
		sys.exit(0)

	with open(argv[1]) as f:
 		data = f.read()

	d = calc_digest(data)

	print d.hexdigest()

if __name__ == "__main__":
        main(sys.argv)
