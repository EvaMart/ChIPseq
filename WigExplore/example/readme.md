# Example:  

We want to check the chromosomes in which the intervals in TestFile.wigFix are located and how many intervals locate in each chromosome.  
TestFile.wigFix contains intervals in chromosomes: chr1, chr1_SDECSD, chr1_DXC1232, chr11 and chr11_XSZ.

**TestFile.wigFix** **:
```
fixedStep chrom=chr1 start=11707 step=1
1
1
1
1
1
1
fixedStep chrom=chr1 start=15667 step=1
1
1
1
1
1
fixedStep chrom=chr1_SDECSD start=23432 step=1
1
1
1
1
1
1
1
... etc ...
```
We run:
```bash
python WigExplre.py TestFile.wigFix
```
**TestFile.wigFix.ExplInfo** is the output:
```
chr1	2
chr1_SDECSD	3
chr1_DXC1232	3
chr11	2
chr11_XSZ	1
```

