#Cheatsheet I: Formatting
#Table of contents:
1. [Deleting things after dot in fist column](#p1)
2. [Deleting lines begining with certain expression](#p2)
3. [Adding an expression at the begining of every line](#p3)
4. [Deleting an expression that appears more that once in a text file](#p4)
5. [Copying lines between two expressions](#p5)
6. [Deleting one column of a text file](#p6)
7. [Deleting several columns of a text file](#p7)
8. [Checking if a bam file has a binary header](#p8)
9. [Subsample bam. Fraction: 0.5](#p9)

Some useful solutions for dealing with files, texts and formats.
####Deleting things after dot in fist column (or another expression inside an expression) <a name="p1"></a>
I want to substitute an expression that contains a dot with the same expression except whats following the dot (using sed).	

**Solution:**		
In sed, put the dot in brackets. 
```shell
sed 's/[.]1//g' input.txt > output.txt
```
Example:		
From:
```
GL174807.1	14618	15080
GL174807.1	13786	13988
GL174807.1	13390	13647
```
to 
```
GL174807	14618	15080
GL174807	13786	13988
GL174807	13390	13647
```
Remember: when using *sed*, if -i not stated, result is shown in screen.
If -i, then the file is modified. If want output separated from intact
input, use `input.txt > output.txt`.
####Deleting lines begining with certain expression. <a name="p2"></a>
There are lines in a text file starting with *#* I want to delete.  

**Solution:**
```sh
grep "^[^#]" input > output
```
Example:
```sh
grep "^[^#]" Mus_musculus.GRCm38.82.gtf > Mus_musculus.GRCm38.82.mod.gtf
```
From:
```sh
eva@foo:~/foo$ head Mus_musculus.GRCm38.82.gtf
#!genome-build GRCm38.p4
#!genome-version GRCm38
#!genome-date 2012-01
#!genome-build-accession NCBI:GCA_000001635.6
#!genebuild-last-updated 2015-09
1	havana	gene	3073253	3074322	.	+	.	gene_id "ENSMUSG00000102693"; gene_version "1"; gene_name "4933401J01Rik"; gene_source "havana"; gene_biotype "TEC"; havana_gene "OTTMUSG00000049935"; havana_gene_version "1";
```
To:
```sh
eva@foo:~/foo$ head Mus_musculus.GRCm38.82.mod.gtf
1	havana	gene	3073253	3074322	.	+	.	gene_id "ENSMUSG00000102693"; gene_version "1"; gene_name "4933401J01Rik"; gene_source "havana"; gene_biotype "TEC"; havana_gene "OTTMUSG00000049935"; havana_gene_version "1";

```

####Adding an expression at the begining of every line. <a name="p3"></a>
I need to add *chr* at the begining of every line.		

**Solution:**
```sh
sed -i 's/^/chr/' file
```
Example:
```sh
sed -i  's/^/chr/' mus.gtf
```
From:
```
1	25000	0.0884027569673359
1	429760	0.168550401010501
1	388441	0.100897722183018
1	623867	0.118182579807373
```
To:
```
chr1	25000	0.0884027569673359
chr1	429760	0.168550401010501
chr1	388441	0.100897722183018
chr1	623867	0.118182579807373
```
####Deleting an expression that appears more that once in a text file.<a name="p4"></a>
I want to delete every *span=1* in a wig file.		

**Solution:**
```sh
sed -e 's/\<span=1\>//g' input.wig > output.wig
```
####Copying lines between two expressions. <a name="p5"></a>
 I need the lines of a wig corresponding to a chromosome. This is, I need
 everything between `fixedStep chrom=chr(n)` and `fixedStep chrom=chr(n+1)`.  
 
 
**Solution:**
 ```bash
sed -n '/fixedStep chrom=chr(n)/,/fixedStep chrom=chr(n+1)/p' allchrom.fix.wig > onechrom.fix.wig
 ```
 ```bash
sed -n '/fixedStep chrom=chr9/,/fixedStep chrom=chr10/p' SRR085462_N_1_sort.fix.wig > fix.9.wig
 ``` 
####Deleting one column of a text file. <a name="p6"></a>
I want to delete column *n*.		

**Solution:**
``` bash
awk '{ $n = ""; print>"new.txt" }' filename
```
For column 2:
```bash
awk '{ $2 = ""; print>"new.txt" }' filename
```
####Deleting several columns of a text file. <a name="p7"></a>
I want to delete columns *n* to *k*.\\
**Solution:**
```bash
cut -fn-k file
cut -f4-13 file  ## prints from the 4th to the 13th
```
####Checking if a bam file has a binary header. <a name="p8"></a>
Sometimes, if the .bam file is truncated (you may have run out of memory while creating it), when trying to process it with a tool, you get: `[bam_header_read] EOF marker is absent`. You have to check if it is complete.   

**Solution:**
```bash
ls *.bam | awk '{print "echo "$1";od -c -N4 "$1}' | bash
```
If everything is fine, you get:
```sh
0000000 037 213 \b 004
```
Another way to see the header: 
```bash
samtools view -H file.bam
```
####Subsample bam. Fraction: 0.5. <a name="p9"></a>
**Solution:**
```bash
samtools view -s 0.5 file.bam -b > 0.0.2.bam
```
The `-b` is very important.