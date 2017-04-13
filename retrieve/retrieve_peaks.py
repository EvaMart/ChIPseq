# -*- coding: utf-8 -*-
from __future__ import division
import sys

#argumentos: <p>  <out_common>

if not len(sys.argv) == 3:
	print('No input or input specified. Format: gene.py <genes.bed> <output name>')
	raise SystemExit


indeces_file=open(sys.argv[2], "r")
lines=[]
for e in indeces_file:
	lineElements=e.split('\t')
	lines.append(int(lineElements[0]))

i=0
all_peaks=open(sys.argv[1], "r")
common_peaks=open('common_peaks.bed', "w")
non_common_peaks=open('non_common_peaks.bed', "w")

i=1
for line in all_peaks:
    if i in lines:
        common_peaks.write(line)
        i+=1
    else:
		non_common_peaks.write(line)
		i+=1
	
