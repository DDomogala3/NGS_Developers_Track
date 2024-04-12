import pysam

#samfile = pysam.AlignmentFile("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/Galaxy117-[HBB_Gene].bam","rb")
#samfile = pysam.AlignmentFile(input("Please provide the Path to the input file: "),"rb")
#regions = (input('Please provide the genomic regions to veiw the file: '))
#bamfile = (input("Please provide the Path to the input file: "))
#chrm_coordinate = (input('Please the chromosome number to perform the pileup on: '))
#start_coordinate = (input('Please provide where you would like the pileup to start: '))
#end_coordinate = (input('Please provide where you would like the pileup to end: '))

def generate_pileup_file(input,contig,start_cord,end_cord,output_file):
    with open(output_file,'w') as f:
        iter = input.pileup(contig,start_cord,end_cord)
        for pileupcolumn in iter:
            print(str("\n coverage at base %s = %s" % (pileupcolumn.pos,pileupcolumn.n)))
            f.write("\n coverage at base %s = %s" % (pileupcolumn.pos,pileupcolumn.n))
            for pileupread in pileupcolumn.pileups:
                if not pileupread.is_del and not pileupread.is_refskip:
            # query position is None if is_del or is_refskip is set.
                    print('\tbase in read %s = %s' %
                      (pileupread.alignment.query_name,
                       pileupread.alignment.query_sequence[pileupread.query_position]))
                    f.write('\tbase in read %s = %s' %
                            (pileupread.alignment.query_name,
                       pileupread.alignment.query_sequence[pileupread.query_position]))
