# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:56:44 2016

@author: lab204
"""
# -*- coding: utf-8 -*-
from __future__ import division

import random
import math
import sys


#argumentos: <g> <p> <common_genes> <out_common> <out_non_common> 

if not len(sys.argv) == 6:
	print('No input or input specified. Format: gene.py <genes.bed> <output name>')
	raise SystemExit


#2 files opened: GENES_, PEAKS_
g=sys.argv[1]
GENES_=open(g,"r")
p=sys.argv[2]
PEAKS_=open(p,"r")
c=sys.argv[3]
COMMON_=open(c,"r")
#PARSING:
Genes=[]
Chr=[]
Strand=[]
TSSs=[]
for e in GENES_:
	LineElements=e.split('\t')
	Genes.append(str(LineElements[0]))
	Chr.append(str(LineElements[1]))
	Strand.append(int(LineElements[3]))
	TSSs.append(int(LineElements[2]))
GENES=[Genes, Chr, Strand, TSSs]

chro=[]
center=[]
for e in PEAKS_:
    LineElements=e.split('\t')
    chro.append(str(LineElements[0]))
    center.append(int(LineElements[1]))
PEAKS=[chro, center]

common_genes=[]
for i in COMMON_:
	LineElements=i.split('\n')
	common_genes.append(LineElements[0])
	
	
	
def ClosestGene(peak_index,Genes, Chr, chro, center, TSSs):
    genes_1Mb=[]
    dist_1Mb=[]
    for gene_index in range(len(Genes)):
        if Chr[gene_index]==chro[peak_index]:
            d=int(center[peak_index]-TSSs[gene_index])
            if abs(d) < 1000000:
                genes_1Mb.append(Genes[gene_index])
                dist_1Mb.append(abs(d))
    if len(dist_1Mb)>=1:
        ind=dist_1Mb.index(min(dist_1Mb)) 
        assigned_gene=genes_1Mb[ind]
        return(assigned_gene)
    else: 
        return

out_comm=sys.argv[4]
common_file=open(out_comm, "w")
out_non_comm=sys.argv[5]
non_common_file=open(out_non_comm, "w")

peak_gene_assig={}

for peak in range(len(center)):
	name=str(peak)
	gene__=ClosestGene(peak,Genes, Chr, chro, center, TSSs)
	peak_gene_assig[name]=gene__
	if gene__ in common_genes:
		common_file.write(str(name)+'\t'+str(chro[peak])+'\t'+str(center[peak])+'\t'+str(gene__)+'\n')
	else:
		non_common_file.write(str(name)+'\t'+str(chro[peak])+'\t'+str(center[peak])+'\t'+str(gene__)+'\n')
