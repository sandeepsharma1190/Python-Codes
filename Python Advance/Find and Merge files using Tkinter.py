# Find and Merge_files_using_Tkinter

#display them in the Scrolling Textbox.
 
#Identify all the ".txt" files in in the current directory and merge them in to merged_file.txt and 
#Show the details in the scrolling text. 

#Merge functionality can merge only ".txt" files.

import os
import shutil
import tkinter
#!pip install tk
from tkinter import *
from tkinter import scrolledtext


#Files search

def file_search(event):
    
    l=[]
    drive="CD"

    for i in range(0,len(drive)):
        print(drive[i])
        if os.path.exists(drive[i]+":\\"):
            l.append(drive[i]+":\\")
            
    print (l)

    str1=txtfld.get()
    extension=str1.split(".")
    
    st.delete("1.0",END)
    st.insert(END, "Drive types  "+ str(l) + "\n")
    st.insert(END, "List of all "+ str1 + " files""\n")
    st.insert(END,"\n")
    st.insert(END, "ABSOLUTE PATH --------- FILE NAME"+"\n"+"\n")

    for drive_type in l:
        for root,dirs,files in os.walk(drive_type):
            for fname in files:
                if(fname.split(".")[-1]==extension[-1]):
                    print(root,fname)
                    print(os.path.join(root,fname))

                    result=root+"  -----  "+fname
                    
                    st.update()
                    st.insert(END,result+"\n")
                    st.insert(END,"\n")


# merge_files() - Merges only ".txt" files in the current directory and output is stored in merged_file.txt

def merge_files(event):
    

    abspth=os.getcwd()
    str1=txtfld.get()
    extension=str1.split(".")
    print(extension)
    
    if (extension[1] == "txt"):
        st.delete("1.0",END)
        st.insert(END, "List of all "+ str1 + " files merged""\n")
        st.insert(END,"\n")
        st.insert(END, "ABSOLUTE PATH OF FILE --------- FILE NAME"+"\n"+"\n")

        df=open(abspth+"\\"+"merged_file.txt","w+")

        for root,dirs,files in os.walk(abspth):
            for fname in files:
                    if(fname.split(".")[-1]== 'txt'):
                        print(root,fname)
                        print(os.path.join(root,fname))

                        result=(root+"  -----  "+fname)
                        st.update()
                        st.insert(END,result+"\n")
                        st.insert(END,"\n")
                        sf = open(root+"\\"+fname, "r")
                        df.write(root+"\\"+fname)
                        df.write(2*"\n")
                        data = sf.read() 
                        df.write(data)
                        df.write(2*"\n")
                        sf.close()

        sf.close()
        df.close()

        mf=open(abspth+"\\"+"merged_file.txt","r+")

        merged_data = mf.read()
#        print(merged_data)

        st.insert(END, "Merged File"+"\n")

        st.insert(END,root+"\\"+"merged_file.txt"+"\n")
        
        st.insert(END,"\n")

        st.insert(END, merged_data)

        mf.close
        
    else:
        print(extension[-1])
        st.delete("1.0",END)
        st.insert(END, "Can merge \".txt\" files only"+ "\n")
    
    
    


    
window=Tk()

# add widgets here

window.title('Search files')
window.geometry("1500x700+10+20")

btn=Button(window, text="File Search")
btn.place(x=120, y=90)
btn.bind('<Button-1>',file_search)

btn=Button(window, text="Merge Files")
btn.place(x=20, y=90)
btn.bind('<Button-1>',merge_files)

lbl1=Label(window,text="ENTER THE FILE NAME")
lbl1.place(x=5,y=50)

txtfld=Entry()
txtfld.place(x=140, y=50)

st = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=120, height=20)
st.place(x=200, y=100)

window.mainloop()