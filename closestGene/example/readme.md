# Example

We have a set of peaks *human.peaks* and a gene annotation *genes*. We want just 10 randomizations (this is a test, for a reliable pvalue, 500 should be used).
  * *human.peaks*:
  ```
  1	25154	0.0884027569673359
1	389260	0.168550401010501
1	430619	0.100897722183018
1	559460	0.118182579807373
1	601208	0.165860940062705
...etc...
  ```
  * *genes*:
  ```
   ENSG00000271782	1	-1	50902978
ENSG00000232753	1	1	103817769
ENSG00000225767	1	1	50927141
ENSG00000202140	1	-1	50965529
ENSG00000207194	1	1	51048076
...etc...
  ```
We run:
```bash
python closestGene.py genes human.peaks scores qvalues 10
```
We get two files as an output:

  * *scores*:
  ```
ENSG00000271782	0
ENSG00000232753	0
ENSG00000225767	2.01503031494
ENSG00000202140	0
ENSG00000207194	6.37635961906
...etc...  
  ```
  * *qvalues*:
  ```
  ENSG00000271782	0.5
ENSG00000232753	0.7
ENSG00000225767	0.0
ENSG00000202140	0.7
ENSG00000207194	0.0
...etc...
  ```