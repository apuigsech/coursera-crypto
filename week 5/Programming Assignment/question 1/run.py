#!/usr/bin/env python

# Coursera Crypto I Problem Solution (Week 5, Question 1)
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
import gmpy2

P = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
G = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
H = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

def trivial_calculate(p, g, h):
	x = 1
	while x <= 2**40:
		if pow(g, x, p) == h:
			return x
		x += 1

def meetinthemiddle_calculate(p, g, h, maxexp=40):
	B = gmpy2.mpz(2**(maxexp/2))
   	g = gmpy2.mpz(g)
	h = gmpy2.mpz(h)
	p = gmpy2.mpz(p)


	middle = {}

	for x1 in range(B):
		middle[gmpy2.divm(h, gmpy2.powmod(g, x1, p), p)] = x1

	for x0 in range(B):
		v = gmpy2.powmod(g, B*x0, p)
		if middle.has_key(v):
			x1 = middle[v]
			return B*x0+x1

	return None


def main(argv):
	x = meetinthemiddle_calculate(P, G, H)
	print "x = {0}".format(x)

if __name__ == "__main__":
        main(sys.argv)