import pysam
from pysam import bcftools

#with open("Galaxy117-[HBB_Gene]_annotations_test_jupyter.vcf","w") as f:
#    Annotation = bcftools.annotate("-c","INFO/GENE,INFO/HGVSG,INFO/SO_TERM","--threads","3","-a","Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz","Galaxy117-[HBB_Gene]_test.vcf.gz","-o","Galaxy117-\[HBB_Gene\]_annotations_test_jupyter.vcf")
#    print(Annotation)
#    f.write(Annotation)
vcf_name = input("What is the VCF name?: ")
vcf_output = input("output name: " )
vcf_name = str(vcf_name)
vcf_output = str(vcf_output)

def Annotate_VCF(input_vcf,output_vcf):
    #annotation_file = str(annotation_file)
    input_vcf = str(input_vcf)
    output_vcf = str(output_vcf)
    print(input_vcf)
    print(output_vcf)
    with open(output_vcf,"w") as f:
        Annotation = pysam.bcftools.annotate("-c","INFO/GENE,INFO/HGVSG,INFO/SO_TERM","--threads",'2',"-a","Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz",input_vcf,"-o",output_vcf)
        print(Annotation)
        f.write(Annotation)
#Annotate_VCF(vcf_name,vcf_output)

Annotate_VCF("Galaxy117-[HBB_Gene]_test.vcf.gz","Galaxy117-[HBB_GENE]_test_annotations_pyfunc.vcf")
