import pysam
from pysam import bcftools
#HBB_gene_pileup = pysam.mpileup("Galaxy117-[HBB_Gene].bam","-r","11:524657-5246555","-o","pileup_test","-f","/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/chr11.fa")
#print(HBB_gene_pileup)

#regions = "11:524657-5246555"
#bamfile = "Galaxy117-[HBB_Gene].bam"
#reference = ("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/chr11.fa")
#reference = "chr11.fa"
def m_pileup_calc(bam_file,output_file,reference):
    with open(output_file,"w") as f:
       pysam_pileup = bcftools.mpileup(bam_file,"-o",output_file,"-f",reference)
       print(pysam_pileup)
       f.write(pysam_pileup)
    #return pysam_pileup
#def m_pileup_calc_no_region(bam_file,output_file):
#    with open()
#m_pileup_calc("Galaxy117-[HBB_Gene].bam","Galaxy117-[HBB_Gene].vcf",regions,reference)

def vcf_calling(input,output):
    with open(output,'w') as f:
        VCF_call = bcftools.call(input,"-o",output,"-c")
        print(VCF_call)
        f.write(VCF_call)
    #return VCF_call
#m_pileup_calc("Galaxy117-[HBB_Gene].bam","output.bcf",reference)
#begin pipeline
#pipe1_pileup = m_pileup_calc("Galaxy117-[HBB_Gene].bam","Galaxy117-[HBB_Gene].bcf",regions,reference)
#output_sam file_name
def samtools_view(input,output):
    with open(output,'w') as f:
        samtools_view = bcftools.view(input,"-o",output)
        print(samtools_view)
        f.write(samtools_view)
#samtools_view(,"output.vcf")
#vcf_calling("output.bcf","output.vcf")

def compress_vcf(input,output):
    with open(output,'wb') as f:
        bcftools_view = bcftools.view(input,"-Oz","-o",output)
        f.write(bcftools_view)

def make_tab_vcf(input,output):
    with open(output,'w') as f:
        bcftools_index = bcftools.index(input,"-c","-f","-o",output)
        f.write(bcftools_index)


#compress_vcf("output.vcf","output.vcf.gz")
#make_tab_vcf("output.vcf.gz","output.vcf.gz.csi")

def Annotate_VCF(input_vcf,output_vcf):
    #annotation_file = str(annotation_file)
    input_vcf = str(input_vcf)
    output_vcf = str(output_vcf)
    print(input_vcf)
    print(output_vcf)
    with open(output_vcf,"w") as f:
        Annotation = pysam.bcftools.annotate("-c","INFO/GENE,INFO/HGVSG,INFO/SO_TERM","--threads",'2',"-a","Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz",input_vcf,"-o",output_vcf,"-e","ALT == '.'")
        print(Annotation)
        f.write(Annotation)
#Annotate_VCF(vcf_name,vcf_output)

#Annotate_VCF("output.vcf.gz","output_annotate.vcf.gz")
#def m_pileup_calc(bam_file,output_file,reference):
#    with open(output_file,"w") as f:
#        pysam_pileup = pysam.mpileup(bam_file,"-o",output_file,"-f",reference)
#        print(pysam_pileup)
#        f.write(pysam_pileup)
#m_pileup_calc(bamfile,"test_output",regions,reference)
