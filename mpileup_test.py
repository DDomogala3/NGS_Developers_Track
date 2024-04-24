import pysam
#HBB_gene_pileup = pysam.mpileup("Galaxy117-[HBB_Gene].bam","-r","11:524657-5246555","-o","pileup_test","-f","/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/chr11.fa")
#print(HBB_gene_pileup)

#regions = "11:524657-5246555"
#bamfile = "Galaxy117-[HBB_Gene].bam"
#reference = ("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/chr11.fa")

def m_pileup_calc(bam_file,output_file,region,reference):
    with open(output_file,"w") as f:
       pysam_pileup = pysam.mpileup(bam_file,"-o",output_file,"-r",region,"-f",reference)
       print(pysam_pileup)
       f.write(pysam_pileup)
#def m_pileup_calc(bam_file,output_file,reference):
#    with open(output_file,"w") as f:
#        pysam_pileup = pysam.mpileup(bam_file,"-o",output_file,"-f",reference)
#        print(pysam_pileup)
#        f.write(pysam_pileup)
#m_pileup_calc(bamfile,"test_output",regions,reference)
