# peak_genes

Given a set of peaks (** *peaks.bed* **), an annotation (** *annotation* **) and a set of genes (** *genes* **), this program returns the peaks in ** *peaks.bed* ** whose closest gene is in the set ** *genes* **.  

This program does two main actions:

1. Makes a peak to gene assignment. Each peak in ** *peaks.bed* ** is assigned the closest gene (according to ** *annotation* ** ).
2. Given a list of genes ** *genes* **, it yields two files:
	  * Peaks assigned a gene in ** *genes* **.
	  * Peaks assigned a gene not in ** *genes* **.


#### Usage
```
python peak_genes.py <g> <p> <common> <output_in_common> <output_not_in_common>
```
#### Input
Required files:
  * **g **: annotation of genes with TSSs in the following format:
```
gene_id	chr	strand	TSS
```
for example:
```
ENSG00000223116	13	-1	23552136
ENSG00000233440	13	1	23708313
ENSG00000207157	13	-1	23726825
ENSG00000229483	13	-1	23744736
```
  * **p**: peaks in format:
```
chr(number only)	summit	score(optional)
```
for example:
```
1	25154	0.0884027569673359
1	389260	0.168550401010501
1	430619	0.100897722183018
1	559460	0.118182579807373
```
  * ** common**: set of common genes. A list of ene_ids.
example: 
```
ENSG00000197587
ENSG00000169946
ENSG00000085276
ENSG00000065675
ENSG00000136158
```
#### Output

  * **output_in_common**: peaks whose closest gene is in set **genes**. Format:
```
index	chr summit gene_id
```
example:
```
28	1	4721320	ENSG00000196581
29	1	4771194	ENSG00000196581
30	1	4773395	ENSG00000196581
31	1	4775031	ENSG00000196581
```
`index`, `chr` and `summit` of peak.
`gene_id` of closest gene.
  * **output_not_in_common**: peaks whose closest gene is not in set **genes**.  Same format as **output_in_common**. Example:
  ```
0	1	25154	ENSG00000243485
1	1	389260	ENSG00000269732
2	1	430619	ENSG00000256186
3	1	559460	ENSG00000223659
```
