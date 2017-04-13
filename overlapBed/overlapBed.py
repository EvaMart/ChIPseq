# -*- coding: utf-8 -*-

"""
Created on Tue Feb  9 21:30:17 2016

@author: eva
"""
# -*- coding: utf-8 -*-
# ----- Parsing peak files ------------------------------------------------------- 

from __future__ import division
import sys
Eva_file=open(sys.argv[1], "r")
Adri_file=open(sys.argv[2], "r")

scaffold_eva={}
start_eva={}
end_eva={}
score_eva={}
adri_score={}
index=0
for e in Eva_file:
    LineElements=e.split('\t')
    index=index +1    
    peak='peak_'+ str(index)
    scaffold_eva[peak]=LineElements[0]
    start_eva[peak]=LineElements[1]
    end_eva[peak]=LineElements[2]
    score_eva[peak]=LineElements[3].split("\n")[0]
    adri_score[peak]='NA'
index=0 

scaffold_adri={}
start_adri={}
end_adri={}
score_adri={}
for e in Adri_file:
    LineElements=e.split('\t')
    index=index +1    
    peak='peak_'+ str(index)
    scaffold_adri[peak]=LineElements[0]
    start_adri[peak]=LineElements[1]
    end_adri[peak]=LineElements[2]
    score_adri[peak]=LineElements[3].split("\n")[0]

# ----- Calculating overlapping peaks------------------------------------------------------- 
L=len(start_eva)
l=len(start_adri)
print('Input files look good, calculating overlapping peaks...')
for e in range(1,L):
    inde='peak_' + str(e)
    eA=start_eva[inde]
    eB=end_eva[inde]
    for i in range(1,l):
        ainde='peak_'+str(i)
        if (scaffold_eva[inde]==scaffold_adri[ainde])==True:
            aA=start_adri[ainde]
            aB=end_adri[ainde]
            if (eA>=aA and eA<=aB)==True:
                adri_score[inde]=score_adri[ainde]
            if (eB>=aA and eB<=aB)==True:
                adri_score[inde]=score_adri[ainde]

#----- writing output--------------------------------------------------------------------------
OutFile=open(sys.argv[3], "w")
for a in range(1,L+1):
    ind='peak_'+str(a)
    OutFile.write(str(scaffold_eva[ind])+'\t'+str(start_eva[ind])+'\t'+str(end_eva[ind])+'\t'+str(score_eva[ind])+'\t'+str(adri_score[ind])+'\n')

    
