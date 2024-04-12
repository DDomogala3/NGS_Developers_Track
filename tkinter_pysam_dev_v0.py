import tkinter as tk

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from pysam_pileup_script_v0 import generate_pileup_file
from pysam_pileup_script_v0 import *
import os
import shutil
#start 524657
#end 5246555
root = Tk()
root.title("NGS Developer's Track APP V0.0")
root.geometry('300x200')
test_samfile = pysam.AlignmentFile("/Volumes/Domogala_ext/ddomogalagatk/data/DDD_WGS/Galaxy117-[HBB_Gene].bam","rb")
def entry():
    global samfile
    samfile = samfile_entry.get()
    outfile_name = outfile_entry.get()
    chrm_coordinate = chrm_coordinate_entry.get()
    start_coordinate = start_coordinate_entry.get()
    end_coordinate = end_coordinate_entry.get()
    sam_file_pysam = pysam.AlignmentFile(samfile)
    chrm_coordinate = str(chrm_coordinate)
    start_coordinate = int(start_coordinate)
    end_coordinate = int(end_coordinate)
    generate_pileup_file(sam_file_pysam,chrm_coordinate,start_coordinate,end_coordinate,outfile_name)
    #label = tk.Label(root, width=25, text = "Barcode")
    #label = Label(root, text = "Barcode")
    #label.pack
samfile = StringVar()
outfile_name = StringVar()
chrm_coordinate = StringVar()
start_coordinate = StringVar()
end_coordinate = StringVar()
samfile_id_label = Label(root, text = 'Samfile Path: ', font = ('Times',13,'bold'))
samfile_entry = Entry(root,textvariable = samfile,font=('Times',13,'normal'))
outfile_name_label = Label(root,text = "Outfile name: ", font = ('Times',13,'bold'))
outfile_entry = Entry(root,textvariable = outfile_name, font = ('Times',13,'bold'))
chrm_coordinate_label = Label(root,text = "Chromosome: ", font = ('Times',13,'bold'))
chrm_coordinate_entry = Entry(root,textvariable = chrm_coordinate, font = ('Times',13,'bold'))
start_coordinate_label = Label(root, text = "Start coordinate: ", font = ('Times',13,'bold'))
end_coordinate_entry = Entry(root,textvariable = start_coordinate, font = ('Times', 13, 'bold')  )
end_coordinate_label = Label(root, text = "End coordinate: ", font = ('Times',13,'bold'))
start_coordinate_entry = Entry(root,textvariable = end_coordinate, font = ('Times', 13, 'bold')  )
samfile_id_label.grid(row=1,column=1)
samfile_entry.grid(row=1,column=2)
outfile_name_label.grid(row=2,column=1)
outfile_entry.grid(row=2,column=2)
chrm_coordinate_label.grid(row=3,column=1)
chrm_coordinate_entry.grid(row=3,column=2)
start_coordinate_label.grid(row=4,column=1)
start_coordinate_entry.grid(row=4,column=2)
end_coordinate_label.grid(row=5,column=1)
end_coordinate_entry.grid(row=5,column=2)


samfile_button = tk.Button(root, text = "1) Enter", command = entry, bg = "white", activebackground = "green")
samfile_button.grid(row=11,column = 2, padx = 6, pady = 20)

#print(barcode1)
#def select_file():
#    label = tk.Label(root, width=25, text = "Quant-it file")
#    label.pack
#    filetypes = (('excel spreadsheet', '*.xlsx'),('All_files','*'))
#    filename = fd.askopenfilename(title ='Select Quant it File', initialdir='/', filetypes=filetypes)
#    barcode_filename = str(barcode) + "_" + filename
#    barcode1 = barcode_id_entry.get()
#    output = str(barcode1) +"_" + "Quant_it_output" + str(datetime) + ".xlsx"
#    dir = output[0:5]
#    if not os.path.exists(dir):
    #    os.mkdir(dir)
    #os.path.join(dir,output)
#    Qubit_calculation(filename,output)

#    shutil.move(output, dir)
    #def bcode_sorter():
    #    for file in os.listdir():
     ##       if file[0:5] == barcode1:
        #        shutil.move(file,dir)
       #         os.unlink(file)
        #    else:
        #        pass

    #find other files with barcode and move them into folder

    #bcode_sorter()
    #barcode1 = barcode_id_entry.get()
    #print(barcode1)
    #file2 = str(barcode1) + "Quant_it_output" + str(datetime) + ".xlsx"
     #root
      #open dialogue box
     # openpyxyl function
     # run program

     # button, execute function


#open_button = tk.Button(root, text = "2) Choose Quant-it File", command = select_file, bg = "white",activebackground = "green")
#open_button.grid(row=10,column = 2,padx = 10,pady = 20 )
#print(barcode)
#close_button = tk.Button(root, text = "3) Quit", command = root.destroy(), bg = "white")
#close_button.grid(row=11, column = 2)

def close_win():
    root.destroy()
close_button = tk.Button(root, text = "3) Close", command = close_win, bg = "white", activebackground = "red")
close_button.grid(row = 8, column = 2)
root.mainloop()
