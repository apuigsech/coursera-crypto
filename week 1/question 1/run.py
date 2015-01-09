#!/usr/bin/env python

# Coursera Crypto I Problem Solution (Week 1, Question 1)
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
import itertools
import operator
from cryptohelper import *

freq_eng = dict(freq_eng, **{' ':15, ':':2, ';':2}) 
charset = ''.join(freq_eng.keys())

def combine_charset(charset):
	comb = {}
	for ch1, ch2 in list(itertools.combinations(charset, 2)):
		comb.setdefault(ord(ch1)^ord(ch2), set()).add(ch1)
		comb.setdefault(ord(ch1)^ord(ch2), set()).add(ch2)
	return comb


def keystream_from_many_time_pad(ct_list, charset):
	ks = [{} for i in range(len(sorted(ct_list, key=len, reverse=True)[0]))]

	comb = combine_charset(charset)

	for ct1, ct2 in list(itertools.combinations(ct_list, 2)):
		for i in range(min(len(ct1),len(ct2))):
			mix = ord(ct1[i])^ord(ct2[i])
			if comb.has_key(mix):
				for ch in comb[mix]:
					mix_1 = chr(ord(ct1[i])^ord(ch))
					mix_2 = chr(ord(ct2[i])^ord(ch))
					ks[i].setdefault(mix_1, 0)
					ks[i].setdefault(mix_2, 0)
					ks[i][mix_1] += freq_eng[ch]
					ks[i][mix_2] += freq_eng[ch]

	# Part of the key can't be solved statistically. So it's hand edited.
	ks[25]['\x7f'] = 1000

	ks_str = ''
	for k in ks:
		if (len(k) > 0):
			ks_str += sorted(k.items(), key=operator.itemgetter(1), reverse=True)[0][0]
		else:
			ks_str += "\x00"

	return ks_str
	

def main(argv):
	with open('ct.txt') as f:
		ct_samples = [line.rstrip().decode('hex') for line in f]

	ks = keystream_from_many_time_pad(ct_samples, charset)
	print strxor(ct_samples[-1], ks)
       

if __name__ == "__main__":
        main(sys.argv)
