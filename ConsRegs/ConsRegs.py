# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:18:49 2016

@author: eva
"""
from __future__ import division
import sys
hgWig=sys.argv[1]
#hgWig='/home/eva/eomes/PARTE2/cons/soft/test.out.txt'
bed_output=sys.argv[2]
#bed_output='/home/eva/eomes/PARTE2/cons/soft/ConsRegs/test.conserved.bed'
thres=sys.argv[3]
thres=float(thres)
#thres=0.9

hgWiggle_out=open(hgWig,"r")
BEDout=open(bed_output, "w")

'''
#	output date: 2016-11-18 18:43:41 UTC
#	constrained by chr names and coordinates in bed list
#	This data has been compressed with a minor loss in resolution.
#	(Worst case: 0.0078125)  The original source data
#	(before querying and compression) is available at 
#		http://hgdownload.cse.ucsc.edu/downloads.html
variableStep chrom=chr1 span=1
20827450	0
20827451	0
20827452	0
20827453	0
20827454	0
20827455	0
20827456	0.23622
20827457	0.228346

'''

prev_score=0

for line in hgWiggle_out:
    LineElement=line.split("\t")
    if LineElement[0]=='#':
        continue
    LineElement=line.split(" ")
    if LineElement[0]=='variableStep':
        chrom_string=LineElement[1].split('=')
        chrom=chrom_string[1]
        pos_in_chr=0
    else:
        LineElement=line.split("\t")
        position=int(LineElement[0])
        score=LineElement[1].split('\n')
        score=float(score[0])
        pos_in_chr=pos_in_chr+1
        if pos_in_chr==1:
            start=position
            prev_score=score
        if prev_score<thres and score>thres: #This is the begining of a conserved region.
            start=position
            prev_score=score
        if prev_score>thres and score>thres:
            prev_score=score
        if prev_score>thres and score<thres:
            end=position-1
            BEDout.write(str(chrom)+'\t'+str(start)+'\t'+str(end)+'\n')
            prev_score=score        

        
        
        
        