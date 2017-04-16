# -*- coding: utf-8 -*-
from __future__ import division

import random
import math
import sys

#argumentos: <g> <p> <scores> <qvalues> <n_permut> <U> <D>

if not len(sys.argv) == 8:
	print('No input or input specified. Format: gene.py <genes.bed> <output name>')
	raise SystemExit

#2 files opened: GENES_, PEAKS_
g=sys.argv[1]
GENES_=open(g,"r")
p=sys.argv[2]
PEAKS_=open(p,"r")
Upstream=open(sys.argv[6], "r")
Downstream=open(sys.argv[7], "r")
#PARSING:
Genes=[]
Chr=[]
Strand=[]
TSSs=[]
for e in GENES_:
	LineElements=e.split('\t')
	Genes.append(str(LineElements[0]))
	Chr.append(str(LineElements[1]))
	Strand.append(int(LineElements[2]))
	TSSs.append(int(LineElements[3]))
GENES=[Genes, Chr, Strand, TSSs]

chro=[]
center=[]
for e in PEAKS_:
    LineElements=e.split('\t')
    chro.append(str(LineElements[0]))
    center.append(int(LineElements[1]))
PEAKS=[chro, center]

U=[]
for e in Upstream:
	LineElements=e.split('\n')
	U.append(int(LineElements[0]))

D=[]
for e in Downstream:
	LineElements=e.split('\n')
	D.append(int(LineElements[0]))
	


def near_genes(u,Genes, Chr, chro, center, TSSs):
    genes_1Mb=[]
    dist_1Mb=[]
    ud_1Mb=[]
    for e in range(len(Genes)):
        if Chr[e]==chro[u]:
            d=int(center[u]-TSSs[e])
            if d>0:
                ud="up"
            else: 
                ud="down"
            if abs(d) < 1000000:
                genes_1Mb.append(Genes[e])
                dist_1Mb.append(abs(d))
                ud_1Mb.append(ud)
    if len(dist_1Mb)>=1:
        ind=dist_1Mb.index(min(dist_1Mb)) ## Este paso es el que hay que 
        # replicar y randomizar
        gene_dist=[genes_1Mb[ind], dist_1Mb[ind], ud_1Mb[ind]]
        return(gene_dist)
    else: 
        return

def near_genes_rand(u,Genes, Chr, chro, center, TSSs):
    genes_1Mb=[]
    dist_1Mb=[]
    ud_1Mb=[]
    for e in range(len(Genes)):
        if Chr[e]==chro[u]:
            d=int(center[u]-TSSs[e])
            if d>0:
                ud="up"
            else: 
                ud="down"
            if abs(d) < 1000000:
                genes_1Mb.append(Genes[e])
                dist_1Mb.append(abs(d))
                ud_1Mb.append(ud)
    ###### RANDOMIZATION  #########
    if len(dist_1Mb)>=1:
	upper=len(dist_1Mb)-1
        ind=random.randint(0,upper)
        gene_dist=[genes_1Mb[ind], dist_1Mb[ind], ud_1Mb[ind]]
        return(gene_dist)
    else: 
        return



    
GENES_dist=[]				
for u in range(len(center)):	
	GENES_dist.append(near_genes(u, Genes, Chr, chro, center, TSSs))
GENES_dist=[x for x in GENES_dist if x is not None]

out=sys.argv[3]
output=open(out, "w")

def fraction(distance, ud, U, D):
    if ud=="up":
        upp=[x for x in U if x < distance]
        n=len(upp)
        return(float(n/len(U)))
    if ud=="down":
        downn=[x for x in D if x < distance]
        n=len(downn)
        return(float(n/len(D)))

def score(gene_ID, GENES_dist):
    score=0
    for i in range(len(GENES_dist)):
        if GENES_dist[i][0]==gene_ID:
            f=fraction(GENES_dist[i][1],GENES_dist[i][2], U, D)
            #print(gene_ID)
            #print(f)
            if f!=0.0:
                score=score-math.log10(f)
    return(score)

Scores=[]
for u in range(len(Genes)):
    sc=score(Genes[u], GENES_dist)
    Scores.append(sc)
    output.write(str(Genes[u])+'\t'+ str(sc) + '\n')
	
	
SCORES=[Genes, Scores]


def randomizations(ran_n, Genes,u, Chr, chro, center, TSSs):
    Scores_random=[]
    for e in range(ran_n):
        Scores=[]
        GENES_dist_rand=[]				
        for u in range(len(center)):	
            GENES_dist_rand.append(near_genes_rand(u, Genes, Chr, chro, center, TSSs))
        GENES_dist_rand=[x for x in GENES_dist_rand if x is not None]
        for u in range(len(Genes)):
            sc=score(Genes[u], GENES_dist_rand)
            Scores.append(sc)
        Scores_random.append(Scores)
    return(Scores_random)

nran=int(sys.argv[5])
Permut_scores=randomizations(nran, Genes,u, Chr, chro, center, TSSs)


qvalout=open(sys.argv[4], "w")

###### Calulculamos el qvalue ######
qvalues=[]
for s in range(len(Genes)):
	gene_scores=[]
	for e in range(nran):
		gene_scores.append(Permut_scores[e][s])
	greater=[x for x in gene_scores if x > Scores[s]]
	qvalue=len(greater)/len(gene_scores)
	qvalout.write(str(Genes[s])+'\t'+str(qvalue)+'\n')
	qvalues.append(qvalue)
