# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:01:25 2016
@author: eva
"""
from __future__ import division
import sys

#BEDin=sys.argv[1]
hgWig=sys.argv[1]
Reada_output=sys.argv[2]

'''
Debugging test files:
#BEDin='/home/eva/eomes/PARTE2/cons/common/common_peaks_hg38.bed'
hgWig='/home/eva/eomes/PARTE2/cons/common/100way/out.txt'
Reada_output='/home/eva/eomes/PARTE2/cons/common/100way/out.rdbl'

#BEDin='/home/eva/eomes/PARTE2/cons/soft/test.bed'
hgWig='/home/eva/eomes/PARTE2/cons/soft/test.out.txt'
Reada_output='/home/eva/eomes/PARTE2/cons/soft/test.2.rdbl'
'''

#BEDfile=open(BEDin, "r")
#BED=[]
chromosomes=[]
hgWiggle_out=open(hgWig,"r")
'''
For debugging pourposes:

BED file parsing
-----------------------------------------------
BED format:
chr1	20827450	20827933	0.215536780509182
chr1	21058129	21058426	0.154029921924593
chr1	23525881	23526039	0.0809625540937227
-----------------------------------------------
peak_n=0 
START=1
END=0
for line in BEDfile:
    peak_data_temp=[]
    peak_n+=1
    LineElement=line.split('\t')
    chrom=LineElement[0]
    start=int(LineElement[1])
    end=int(LineElement[2])
    name='peak_'+ str(peak_n)
    peak_data_temp.append(name) # peak name
    peak_data_temp.append(LineElement[0]) #the chromosome
    peak_data_temp.append(start) #start
    peak_data_temp.append(end) #end
    if chromosomes==[]:
        START=1
    elif chrom not in chromosomes:
        chromosomes.append(chrom)
        START=1
    else:
        START=END+1
    peak_data_temp.append(START) #START
    END=START+end-start
    peak_data_temp.append(END) #START
    BED.append(peak_data_temp)
'''
# hgWiggle output file parsing
"""
variableStep chrom=chr1 span=1
20827450	0
20827451	0
20827452	0
"""
#t=open('debug', "w")
WIG=[]
SameChr=[]
WigLoc=[]
WIGLoc=[]
Wig_chromosomes=[]
for line in hgWiggle_out:
    LineElement=line.split("\t")
    if LineElement[0]=='#':
        continue
    LineElement=line.split(" ")
    if LineElement[0]=='variableStep':
        chrom_string=LineElement[1].split('=')
        if chrom_string[1] not in Wig_chromosomes: # If new chromosome
            #print('count of bases:' + str(len(SameChr)))
            #print('new chr:' + str(chrom_string[1]))            
            if Wig_chromosomes!=[]:
                WIG.append(SameChr) # The previous chromosome is added to WIG
                WIGLoc.append(WigLoc)
            Wig_chromosomes.append(chrom_string[1]) # We add the new to the list of chrs
            SameChr=[] # Create the new vector for the new chr
            SameChr.append(chrom_string[1]) #The first value of the vector is the name of the chr
            WigLoc=[] # Create the new vector for the new chr
            WigLoc.append(chrom_string[1]) #The first value of the vector is the name of the chr
    else:
        LineElement=line.split("\t")
        WigLoc.append(str(LineElement[0]))
        score=LineElement[1].split('\n')
        SameChr.append(float(score[0])) # We add the score
        #t.write(str(float(score[0]))+'\n')
WIG.append(SameChr) # The last chromosome in the output is added to WIG
WIGLoc.append(WigLoc)

'''
Desired format:
peak    bp  phastCons
peak_1  -13 0.01
peak_1  -12 0.001
...
'''
#Reading wig to find peaks by step. If the step between two positions is > 1, 
#it is considered a new peak.
readable=open(Reada_output, "w")
readable.write('Peak \t chr \t phastCons \n')
#Peak by peak:
peak=1
for e in range(len(Wig_chromosomes)):
    for i in range(len(WIG[e])-1):
        if i==0:
            peak_name='peak_'+str(peak)
            readable.write(str(peak_name)+'\t'+str(WIG[e][0])+'\t'+str(WIG[e][i+1])+'\n')
        else:
            current_loc=float(WIGLoc[e][i+1])
            previous_loc=float(WIGLoc[e][i])
            if current_loc==previous_loc+1:
                peak_name='peak_'+str(peak)
                readable.write(str(peak_name)+'\t'+str(WIG[e][0])+'\t'+str(WIG[e][i+1])+'\n')
            else:
                peak=peak+1
                peak_name='peak_'+str(peak)
                readable.write(str(peak_name)+'\t'+str(WIG[e][0])+'\t'+str(WIG[e][i+1])+'\n')
    peak=peak+1
                
        
        
        
        

