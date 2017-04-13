## overlapBed.py  

This program takes two bed files as an input and returns a bed file that contains peaks in file1 and, next to the score of every peak in file1, the score of  the (it will show only one if there are several) peak in file2 that overlaps in at least one base with it. If there is no overlap, score in file2 = 'NA'.  
Usage:  
```bash
python overlapBed.py <file1.bed> <file2.bed> <output.bed>
```
Input files:
- file1.bed and file2.bed: bed format file. At least 4 fields separated by tabs:
```
chromosome	start	end	score
```

Output file:
- output.bed: bed format file. Five fields: 
```
chromosome	start1	end1	score1	score2
```
     * Chromosome: chromosome.
     * start1: start of peak in file1.
     * end1: end of peak in file1.
     * score1: score of peak in file 1. 
     * score2: score of overlaping peak in file2. If there is no overlapping peak in file2, score2='NA'.


