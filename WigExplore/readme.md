# WigExplore

This program explores the intervals of a given wigFix file and returns the chromosomes they belong to and the frecuency.

### Usage:
The only argument needed is the wig file we want to explore.
```bash
pyhton WigExplore.py <fixed_step_input>
```
### Files:
#### Input file:
A **fixedStep Wig** file (e.i **input.wig**). This format:
```
fixedStep	chrom=chrN start=position  step=stepInterval	[span=windowSize]
  dataValue1
  dataValue2
  ... etc ...
```
Example:
```
fixedStep chrom=chr3 start=400601 step=100
11
22
33
```
or 
```
fixedStep chrom=chr3 start=400601 step=100 span=5
11
22
33 
```
#### Output file:
It will be called as the input followed by *.ExplInfo* (e.i **input.wig.ExplInfo**). It looks:
```
chrN	frecuency
chrN+1	frecuency
... etc ...
```
frecuency=number of inervals in a given chromosome
