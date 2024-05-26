Code for final project of NGS Developers Track course at MDL, May, 2024
NGS App developers BAM to annotated vcf plan

input is BAM with .bai file with reference genome.
Along with the reference FASTA file

*One issue is the reference FASTA file has the "chr" listed as ch when it needs to be listed
as "ch"

Maybe open the reference genome and change all "ch" names to "chr11"

Possibly have "if" statement to choose whether chromosome region is selected or annotate

Name output annotated COSMIC vcf file
