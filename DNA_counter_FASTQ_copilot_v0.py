import tkinter as tk
from tkinter import filedialog

def DNA_count(text):
    A = 0
    T = 0
    G = 0
    C = 0
    SUM = 0
    for i in text:
        if i == "A":
            A += 1
            SUM += 1
        elif i == "T":
            T += 1
            SUM += 1
        elif i == "G":
            G += 1
            SUM += 1
        elif i == "C":
            C += 1
            SUM += 1
        else:
            pass
    A_percent = round(A/SUM * 100, 2)
    T_percent = round(T/SUM * 100, 2)
    G_percent = round(G/SUM * 100, 2)
    C_percent = round(C/SUM * 100, 2)
#    return A, T, G, C, SUM, A_percent, T_percent, G_percent, C_percent
    return A_percent, T_percent, G_percent, C_percent
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("FASTQ files", "*.fastq"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            sequences = []
            while True:
                header = file.readline().strip()  # Read the header line (starts with '@')
                if not header:
                    break  # End of file
                sequence = file.readline().strip()  # Read the sequence line
                file.readline()  # Skip the '+' line
                file.readline().strip()  # Skip the quality score line
                
                sequences.append(sequence)
            # Join all sequences into one string for counting
            text = ''.join(sequences)
            label.config(text="A: %s T: %s G: %s C: %s" % DNA_count(text))

window = tk.Tk()
window.title("DNA Base Percentage Counter")

button_open = tk.Button(window, text="Open FASTQ File", command=open_file)
button_open.pack()

label = tk.Label(window, text="A: 0 T: 0 G: 0 C: 0")
label.pack()

window.mainloop()
