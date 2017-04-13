**overlapBed.py**

This program takes two bed files as an imput and return the peaks in file1 and the score of the peak in file2 that overlaps it. If there is not overlap, score in file2 = 'NA'. 

Usage: overlapBed.py <file1.bed> <file2.bed> <output.bed>

Input files:
file1.bed: bed format file. At least 4 fields: chromosome, start, end, score.
file2.bed: bed format file. At least 4 fields: chromosome, start, end, score.

Output file:
output.bed: bed format file. Five fields: 
	chromosome (or scaffold).
	start: start of peak in file1.
	end: end of peak in file1.
	score1: score of peak in file 1. 
	score2: score of overlaping peak in file2. If there is no overlapping peak in file2, score2='NA'.


