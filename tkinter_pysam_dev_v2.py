import tkinter as tk

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from mpileup_test_DDD_WGS import m_pileup_calc
from mpileup_test_DDD_WGS import *
import os
import shutil
#from bioblend.galaxy import GalaxyInstance

#gi = GalaxyInstance(url='https://usegalaxy.eu/', key='318244ca7f6ccaba8748d71942ad5f60')
#start 524657
#end 5246555
#history = (gi.histories.get_histories()[0])

#print(history.get_datasets())
root = Tk()
root.title("NGS Developer's Track APP V2.0")
root.geometry('300x200')
#test_samfile = pysam.AlignmentFile("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/Galaxy117-[HBB_Gene].bam","rb")
#reference = pysam.FastaFile("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/Galaxy102-[hg19_v0_Homo_sapiens_assembly19.fasta].fasta")
def entry():
    global bamfile
    bamfile = bamfile_entry.get()
    outfile_name = outfile_entry.get()
    #chrm_coordinate = chrm_coordinate_entry.get()
    #start_coordinate = start_coordinate_entry.get()
    #end_coordinate = end_coordinate_entry.get()
    region = region_entry.get()
    reference = reference_entry.get()
    #bam_file_pysam = pysam.AlignmentFile(samfile)
    bamfile = str(bamfile)
    reference = str(reference)
    #chrm_coordinate = str(chrm_coordinate)
    #start_coordinate = int(start_coordinate)
    #end_coordinate = int(end_coordinate)
    region = str(region)
    #dir_name = tk.filedialog.askdirectory()
    #shutil.copy2(outfile_name,dir_name)
    #start 524657
    #end 5246555
    #reference = "https://usegalaxy.eu/api/datasets/4838ba20a6d8676503e4f1cf8bb6b22a/display?to_ext=fasta"

    #generate_pileup_file(sam_file_pysam,chrm_coordinate,start_coordinate,end_coordinate,outfile_name)
    m_pileup_calc(bamfile,outfile_name,reference)
    #core_filename = str(outfile_name[0])
    #print(core_filename)
    #out_vcf = outfile_name.strip(".bcf") + ".vcf"
    vcf_calling(outfile_name,"output.vcf")
    compress_vcf("output.vcf","output.vcf.gz")
    make_tab_vcf("output.vcf.gz","output.vcf.gz.csi")
    Annotate_VCF("output.vcf.gz","output_annotate.vcf")


    dir_name = tk.filedialog.askdirectory()
    shutil.copy2("output_annotate.vcf",dir_name)

    #dir_name = tk.filedialog.askdirectory()

    #label = tk.Label(root, width=25, text = "Barcode")
    #label = Label(root, text = "Barcode")
    #label.pack
bamfile = StringVar()
outfile_name = StringVar()
region  = StringVar()
reference = StringVar()
#chrm_coordinate = StringVar()
#start_coordinate = StringVar()
#end_coordinate = StringVar()
bamfile_id_label = Label(root, text = 'Bamfile Path: ', font = ('Times',13,'bold'))
bamfile_entry = Entry(root,textvariable = bamfile,font=('Times',13,'normal'))
outfile_name_label = Label(root,text = "Outfile name: ", font = ('Times',13,'bold'))
outfile_entry = Entry(root,textvariable = outfile_name, font = ('Times',13,'bold'))
#chrm_coordinate_label = Label(root,text = "Chromosome: ", font = ('Times',13,'bold'))
#chrm_coordinate_entry = Entry(root,textvariable = chrm_coordinate, font = ('Times',13,'bold'))
#start_coordinate_label = Label(root, text = "Start coordinate: ", font = ('Times',13,'bold'))
#end_coordinate_entry = Entry(root,textvariable = start_coordinate, font = ('Times', 13, 'bold')  )
#end_coordinate_label = Label(root, text = "End coordinate: ", font = ('Times',13,'bold'))
#start_coordinate_entry = Entry(root,textvariable = end_coordinate, font = ('Times', 13, 'bold')  )
region_id_label = Label(root, text = "Region: ", font = ('Times',13, 'bold'))
region_entry = Entry(root, textvariable = region, font = ('Times', 13, 'bold'))
reference_id_label = Label(root, text = "Reference: ", font = ('Times',13, 'bold'))
reference_entry = Entry(root, textvariable = reference, font = ('Times', 13, 'bold'))

bamfile_id_label.grid(row=1,column=1)
bamfile_entry.grid(row=1,column=2)
outfile_name_label.grid(row=2,column=1)
outfile_entry.grid(row=2,column=2)
region_id_label.grid(row=3,column=1)
region_entry.grid(row=3,column=2)
reference_id_label.grid(row=4,column=1)
reference_entry.grid(row=4, column=2)
#chrm_coordinate_label.grid(row=3,column=1)
#chrm_coordinate_entry.grid(row=3,column=2)
#start_coordinate_label.grid(row=4,column=1)
#start_coordinate_entry.grid(row=4,column=2)
#end_coordinate_label.grid(row=5,column=1)
#end_coordinate_entry.grid(row=5,column=2)
#dir_name = tk.filedialog.askdirectory()
#outfile = str(outfile_name)

#shutil.copyfile(outfile_name,dir_name)
#outfile_name = dir_name + outfile_name
bamfile_button = tk.Button(root, text = "1) Enter", command = entry, bg = "white", activebackground = "pink")
bamfile_button.grid(row=11,column = 2, padx = 6, pady = 20)
#dir_name = tk.filedialog.askdirectory()
#shutil.copyfile(outfile_name,dir_name)


def close_win():
    root.destroy()
close_button = tk.Button(root, text = "2) Close", command = close_win, bg = "white", activebackground = "red")
close_button.grid(row = 8, column = 2)
root.mainloop()
