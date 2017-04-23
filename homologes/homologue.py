# -*- coding: utf-8 -*-
from __future__ import division

import math
import sys

if not len(sys.argv) == 5:
	print('No input or input specified. Format: gene.py <genes.bed> <output name>')
	raise SystemExit


#2 files opened: DICC input output X/Z/H
dictionary=sys.argv[1]
DICC_=open(dictionary,"r")
inp=sys.argv[2]
INP_=open(inp, "r")
out=sys.argv[3]
OUT_=open(out, "w")

specie=sys.argv[4]

dicc={}
if specie=='X':
	print('xenopus to human')
	for e in DICC_:
		LineElements=e.split('\t')
		dicc[str(LineElements[1])] = str(LineElements[0])
		
if specie=='Z':
	print('zebrafish to human')
	for e in DICC_:
		LineElements=e.split('\t')
		gene=LineElements[2].split('\n')
		dicc[str(gene[0])] = str(LineElements[0])

if specie=='H':
	print('human to human')
	for e in DICC_:
		LineElements=e.split('\t')
		dicc[str(LineElements[0])] = str(LineElements[0])
	
for i in INP_:
	LineElements=i.split('\n')
	ID=dicc.get(str(LineElements[0]))
	OUT_.write(str(ID)+'\n')
    
