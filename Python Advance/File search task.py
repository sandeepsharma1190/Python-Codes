# File search task

import os
import string
import tkinter as tk
from tkinter.messagebox import showinfo

def drives():
    """
    This function returns a list of drives available in a system
    """
    try:
        drive = string.ascii_uppercase
        valid_drives = []
        for each_drive in drive:
            if os.path.exists(each_drive+":\\"):
               valid_drives.append(each_drive+":\\")
    except Exception as e:
        print('The error encountered in drives function is',e)
    finally:
        return valid_drives

def search_file(filename):
    """
    This function searches for a file name in all the drives of the computer.
    
    Argument to be passed in a string, which is a part of the file name or the 
    file extension.
    eg. Passing 'test' as an argument will return all the files with 'test' 
        in the file name.
        Passing '*.docx' will return all the files with docx extension.
    
    This is a generator function and returns the result set having the directory 
    and file as a generator
    """
    # default search for extension as False
    search_ext = False
    filename = filename.casefold()
    
    # Search will be done based on extension if the user has entered *.ext
    # where ext can be any extension like txt,docx,mp3,avi,xlsx etc.
    if filename.startswith('*.'):
        extension = filename.replace('*.','')
        search_ext = True
    
    # Get all the drives present on the desktop into a list
    all_drives=drives()
    
    for drive in all_drives:
        for path, dirs, files in os.walk(drive):
            for file in files:
                if (search_ext and file.casefold().endswith(extension)) or ((not search_ext) and filename in file.casefold()):
                    yield(path+'\\'+file)

                    
def merge_files(search_results,ext):
    """
    This function will merge the files with supplied extension
    from the search results. It will write the contents to a new
    file 'merged file' in the current working directory
    
    Arguments - 
        search_results - a generator function with the search results
        ext            - extension of the files to be merged. It supports the below
                         mentioned extensions
                         txt
    """
    lst = []
    f=open('merged file.txt','w')
    for i in search_results:
        if i.casefold().endswith('.'+ext):
            src=open(i,'r')
            f.write(src.read())
            src.close()
            lst.append(i)
    f.close()
    return lst

def validate_contents():
    """
    This function checks if user has entered data on the search
    window. If the user has entered the data then call search_file
    to search for file in all the drives.
    
    The search results are displayed on the search window.
    """
    search = searchtext.get()
    T.configure(state='normal')
    T.delete('1.0', tk.END)
    T.configure(state='disabled')
    if search.strip() != '':
        search=search_file(search.strip())
        num = 0
        for i in search:
            T.configure(state='normal')
            T.insert(tk.END,i+'\n')
            T.configure(state='disabled')
            num += 1
        showinfo("Search results","Total number of files found : "+str(num))
    else:
        showinfo("Search results","Enter a file to be searched")

def validate_merge():
    """
    This function checks if user has entered data on the search
    window. If the user has entered the data then call merge_files
    to search for file in all the drives. All the .txt files will
    be merged to 'merged file.txt'
    
    The merged source files will be displayed in a popup window.
    """

    search = searchtext.get()
    if search.strip() != '':
        files=''
        files_merged = merge_files(search_file(search.strip()),'txt')
        for i in files_merged:
            files += i + '\n'
        if files == '':
            files = 'No .txt files were found for merging'
        showinfo("The below files were merged to 'merged file.txt'",files)
    else:
        showinfo("Merge results","Enter the file name to be searched and merged")

window = tk.Tk()
# to rename the title of the window
window.title("Desktop Search")
# label the search entry field
tk.Label(window,text='Enter file to be searched').grid(row=0)
searchtext=tk.Entry(window,width = 150)
searchtext.grid(row=0, column=1)
tk.Label(window,text='Search results--->').grid(row=1)
tk.Button(window,text='Search',command=validate_contents).grid(row=0,column=2)
T = tk.Text(window, height=25, width=150)
T.grid(row=1,column=1)
T.configure(state='disabled')

tk.Button(window,text="Merge .txt files from search results", fg="blue",command=validate_merge).grid(row=2,column=1)
tk.Button(window,text="QUIT", fg="red",command=window.destroy).grid(row=3,column=2)

tk.mainloop()