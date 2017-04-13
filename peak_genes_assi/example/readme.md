# Example

We have a set of human peaks called *human.peaks.y* and a set of genes *common_regH.txt*. We use *hg19.filt.2.txt* as annotation. This is:

  * g: *hg19.filt.2.txt*
  * p: *human.peaks.y*
  * common: *common_regH.txt*
  * peak_gene: *peak_genes.py*
  * output_in_common: *peaks_common_genes_HXZ*
  * output_not_in_common: *peaks_no_common_genes_HXZ*

We run:
```bash
python peak_genes.py hg19.filt.2.txt human.peaks.y common_regH.txt peaks_common_genes_HXZ peaks_no_common_genes_HXZ
```
*peaks_common_genes_HXZ* and *peaks_no_common_genes_HXZ* are generated.
