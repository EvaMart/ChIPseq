# retrieve_peaks
Used in tandem with peak_gene.py. 
This program retrieves, from file **peaks**, the peaks in **output_in_common**. **output_in_common** is one of peak_gene.py outputs.

#### Usage
```
python retrieve.py <peaks> <output_in_common> 
```
#### Input
  * **peaks**: a bed file. Format:
```
chr	start	end	score
```
Example:
```
chr1	25077	25231	0.0884027569673359
chr1	389103	389418	0.168550401010501
chr1	430482	430757	0.100897722183018
chr1	559354	559567	0.118182579807373
```
  * **output_in_common**: peak_gene.py output. For example:
  ```
  28	1	4721320	ENSG00000196581
29	1	4771194	ENSG00000196581
30	1	4773395	ENSG00000196581
31	1	4775031	ENSG00000196581

  ```
  
  #### Output
  * **common_peaks.bed**: contains the peaks in **peaks** that are also in **output_in_common**. Example:
  ```
  chr1	4540149	4540494	0.175631805014484
chr1	4721056	4721584	0.258015054407893
chr1	4770930	4771459	0.283758510799411
chr1	4773260	4773531	0.1423654947299  
  ```
  * **non_common_peaks.bed**: contains the peaks in **peaks** that are not in **output_in_common**.
  

