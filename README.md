Code for final project of NGS Developers Track course at MDL, May, 2024
NGS App developers BAM to annotated vcf plan

input is BAM with .bai file with reference genome.
Along with the reference FASTA file

*One issue is the reference FASTA file has the "chr" listed as ch when it needs to be listed
as "ch"
Code WILL run with the fill reference genome from UCSC genome browser. However, file is too large (3 Gb) to include in desktop app. 


Maybe open the reference genome and change all "ch" names to "chr11"

Possibly have "if" statement to choose whether chromosome region is selected or annotate

Name output annotated COSMIC vcf file

In the future look into Google cloud functtions to work with streamlit

