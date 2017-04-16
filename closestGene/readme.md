# closestGene
***closestGene*** computes the regulatory potential, as defined by
[Sikora-Wohlfeld *et al.* 2013][1] (*ClosestGene* method), of a set of genes given a set of peaks. 
In addition, ***closestGene*** computes the qvalue of the regulatory score associated to each gene. A null distribution is built per gene by randomly assigning peaks to the gene and computing the likelyhood of the score previously calculated. 

### Usage
```bash
python closestGene.py <genes> <peaks> <scores.name> <qvalues.name> <n_rand>
```
  * `<genes>`: file containing the annotation of genes of which regulatory potential will be computed (full annotations).
  * `<peaks>`: file containing the peaks.
  * `<scores.name>`: scores output file name
  * `<qvalues.name>`: qvalues output file name
  * `<n_rand>`: number of randomizations for the construction of the null distribution for pvalue computation. Recommended: 500. Greater numbers of randomizations give same results as 500.
  
### Input files:

#### genes
Aannotation of genes with TSSs in the following format:
```
gene_id	chr	strand	TSS
```
for example:
```
ENSG00000271782	1	-1	50902978
ENSG00000232753	1	1	103817769
ENSG00000225767	1	1	50927141
```

#### peaks

Peaks in format:
```
chr(number only)	summit	score(optional)
```
Example:
```
1	25154	0.0884027569673359
1	389260	0.168550401010501
1	430619	0.100897722183018
```

### Output
Two files, one containing the scores and a second one containing the qvalues of every gene in `<genes>` file.
#### scores

Format:

```
gene_id	score
```
Example:
```
ENSG00000271782	0
ENSG00000232753	0
ENSG00000225767	2.01503031494
ENSG00000202140	0
ENSG00000207194	6.37635961906
```
####qvalues 
Format:
```
gene_id	qvalue
```
Example:
```
ENSG00000271782	0.5
ENSG00000232753	0.7
ENSG00000225767	0.0
ENSG00000202140	0.7
ENSG00000207194	0.0
```



[1]: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003342
