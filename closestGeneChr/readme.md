# closestGeneChr
** *closestGeneChr *** was written for computing closestGene scores, regulatory potential, as defined by [Sikora-Wohlfeld *et al.* 2013][1] (*ClosestGene* method), and their pvalues, given a set of peaks by chromosome. Peaks and scores of each chromosome in a different BED and annotaion files respectively. 
The difference with ** *closestGene* ** is that ** *closestGeneChr* ** does not generate a distribution of occupation around TSS, but uses alread generated data that need to be provided as input. Note that a  distribution of occupation around TSS is characteristic of a ChIP-seq experiment. Every chromosme of a same experiment uses the same distribution, generated using all the chromosomes in the experiment (very memory demanding).
### Usage
```bash
python closestGene.py <genes> <peaks> <scores> <pvalues> <n_rand> <up> <down>
```
  * `<genes>`: file containing the annotation of genes of which regulatory potential will be computed (full annotations).
  * `<peaks>`: file containing the peaks.
  * `<scores.name>`: scores output file name
  * `<qvalues.name>`: qvalues output file name
  * `<n_rand>`: number of randomizations for the construction of the null distribution for pvalue computation. Recommended: 500. Greater numbers of randomizations give same results as 500.
  * `<up>`: distance to the closest TSS of peaks downtream to that TSS.
  * `<down>`: distance to the closest TSS of peaks upstream to that TSS.
  
### Input
#### *genes*
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

#### *peaks*

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
#### *up* and *down*
List of absolute distances to the TSS:
```
distance_1
distance_2
distance_3
...etc...
```
Example:
``` 
15134
455234
461581
...etc...
```

### Output
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

