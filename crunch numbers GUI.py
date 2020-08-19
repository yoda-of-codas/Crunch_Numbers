import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg
from tkinter import filedialog



open('Crunch_history.bakel','a')

def browseFiles(nb):
        filename = filedialog.askopenfilename(initialdir = "/", title= 'Select a File to Crunch',filetypes = (("Text files","*.txt"),("all files","*.*")))
        nb.insert(0,filename)
        return filename

def saveas():
        
    
def load(nb,file):
    try:
        numdata = [float(x) for x in open(nb.get(),'r').read().strip().replace(',',' ').split(' ')]
    except:
        msg.showwarning('Input File Error','Invalid file or file format\n\n1. Ensure that the file exists\n\n2. Ensure all data within the file follows the standard format of spaces with spacebar or comma')
    else:
        done(numdata,file)
    
def parse(seq):
    try:
        numdata = [float(x) for x in scrin.get(1.0,'end').strip().replace(',',' ').split(' ')]
    except:
        msg.showwarning('Bakel with the Aid','Invalid Number or Entry Format\nPlease enter only numbers\nSpaced with either spacebar or comma')
    else:
        done(numdata,seq)
         
def history():
    H = open('Crunch_history.bakel').read()
    win2 = tk.Tk()
    win2.resizable(False,False)
    win2.geometry("+70+70")
    win2.title('History')
    
    #Scrolled Text
    label3= ttk.LabelFrame(win2,text='History List')
    label3.grid(column=0, row=0, padx= 10, pady= 5)
    scr2 = scrolledtext.ScrolledText(label3, width=30, height=25, wrap=tk.WORD)
    scr2.grid(column=0,row=0)
    scr2.insert('1.0', H)
    scr2.configure(state='disabled')
    
def clear():
    
    
def about():
    msg.showinfo('Python as the language, Thank Monty','Crunch Numbers is the first\
 major GUI project by Bakel with python\nAs opposed to over 500 lines in Java this runs on 166 approx.\
 python code lines.\n2020')

def _help():
    msg.showinfo('Yoda  come  guide  \'em:::','Well the first tab is where you can enter your data on the fly and crunch the numbers by entering it in the textbox and clicking crunch.\n\nYour numbers should be seperated by single spacebar and commas ')
    
def _quit():
    win.quit()
    win.destroy()
    exit()
    
def enter():
    try:
        numb = int(nb.get())
    except:
       msg.showwarning('Error','Invalid Input')
    else:
        nb.delete(0,'end')
        #print(numb)
        numdata.append(numb)
        return numdata

def done(numdata,tab):
    n=len(numdata)
    product,summ,i,numbers=1,0,0,''
    even,odd,ec,oc = '','',0,0
    while i<n:
        summ+=numdata[i]
        product*=numdata[i]
        numbers = numbers + str(numdata[i]) + ' '
        
        if numdata[i]%2==0: #and numdata[i]!=0:
            even = even + str(numdata[i])+' '
            ec+=1
        else:
            odd = odd + str(numdata[i])+' '
            oc+=1
        i+=1
    evens = '\nYou had '+str(ec)+' even numbers: '+even
    odd = '\nYou had '+str(oc)+' odd numbers: '+odd
    avg = '\nAverage = '+str(round(summ/n,4))
    result = 'You entered '+str(n)+' numbers:\n'+numbers+'\nSum = '+str(round(summ,4))+'\nProduct = '+str(round(product,4))+'\
'+avg+evens + odd
    #Scrolled Text
    label2= ttk.LabelFrame(tab,text=t1)
    label2.grid(column=0, row=2, padx= 10, pady= 5)
    scr = scrolledtext.ScrolledText(label2, width=30, height=10, wrap=tk.WORD, padx = 10,pady=10)
    scr.grid(column=0, columnspan=3)
    
    scr.insert('1.0', result)
    scr.configure(state='disabled')
    numdata.clear()
    with open('Crunch_history.bakel','a') as textfile:
        textfile.write(result+'\n\n')

t1 = ''#jus a somefin to lockup
#Main Window
win = tk.Tk()
win.resizable(False,False)
win.title('Crunch Numbers')
win.geometry("+70+70")

win.configure(width = '259',height='200')

#Menu
mb=Menu(win)
win.config(menu=mb)

file_menu = Menu(mb,tearoff=0)
mb.add_cascade(label='More',menu=file_menu)
file_menu.add_command(label='History',command=history)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)

help_menu = Menu(mb,tearoff=0)
mb.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Help',command=_help)
help_menu.add_command(label='About', command=about)

#Tab Control
tabcontrol = ttk.Notebook(win)
seq = ttk.Frame(tabcontrol)
file = ttk.Frame(tabcontrol)
tabcontrol.add(seq, text='Sequence')
tabcontrol.add(file, text='File of numbers')
tabcontrol.pack(expand = 1,fill = 'both')

filelabel = ttk.LabelFrame(file, text = 'Browse to the file \ncontaining the sequence of numbers\nspaced by spaces or comma')
filelabel.grid(column=0, row=1, padx=10, pady=10)

nb = ttk.Entry(filelabel, width=35)
nb.grid(column=0, row=0)
nb.focus()

newlabel = ttk.LabelFrame(filelabel, text="")
newlabel.grid(column=0,row=1)
browse = ttk.Button(newlabel, text= "Browse", command= lambda: browseFiles(nb))
browse.grid(column=0,row=0)

crunch = ttk.Button(newlabel, text= "Done, Crunch", command= lambda: load(nb,file))
crunch.grid(column=1,row=0)
#Another Label
labell= ttk.LabelFrame(seq, text='Enter your numbers in series \nseperated by coma or space,\nPress done when finished')
labell.grid(column=0, row=1, padx= 10, pady= 10)

scrin = scrolledtext.ScrolledText(labell, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
scrin.grid(column=0,row=0 ,columnspan=3)

sim33 = ttk.Button(labell, text= "Done, Crunch", command= lambda: parse(seq))
sim33.grid(column=0, row=2)
#Number box
for child in filelabel.winfo_children():
        child.grid_configure(padx=8, pady=4)
for child in labell.winfo_children():
        child.grid_configure(padx=8, pady=4)

win.mainloop()
