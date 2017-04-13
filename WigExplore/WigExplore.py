# -*- coding: utf-8 -*-

"""
Este programa explora los cromosomas de un archivo wigFix y devuelve su orden 
y número en el fichero.
El wigFix para el que se crea este programa contiene PhastCons scores entre mamíferos
con humanos.
"""

from __future__ import division
import sys

# El único argumeto necesario es el archivo wigFix a explorar.

# Usage:WigExplore.py <wigFix>

Wig_=open(sys.argv[1], "r") # Abrimos el wig
chrom=[] # En esta lista se van registrando los cromosomas que vamos encontrando
N=[] # En esta lista quedará registrado el número de veces que aparece cada cromosoma.
i=-1 # index de la exploración intrachromosome

# Ejemplo formato de un wigFix: 
# fixedStep chrom=chr3 start=11707 step=1

# Empezamos a explorar el archivo línea por línea.
for line in Wig_:
	LineElements=line.split(" ")
	if LineElements[0]=='fixedStep':
		Chr=LineElements[1].split("=")
		chromosome=Chr[1]
		if chromosome not in chrom:
			chrom.append(str(chromosome))
			i=i+1
			N.append(1)		
		else:
			N[i]=N[i]+1

# Las listas se sacan a un archivo:
outFile=str(sys.argv[1])+'.ExplInfo'
out=open(outFile, "w")
for e in range(len(chrom)):
	out.write(str(chrom[e])+'\t'+str(N[e])+'\n')

			
