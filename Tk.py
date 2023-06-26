from tkinter import *
from tkinter.font import Font
import timeit
from organize import *
from tkinter import messagebox


root=Tk()
root.title('Gift')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.resizable(0,0)

base_font=Font(family='Cambria',size=13)
main_box_font=Font(family='Calibri',size=13)
#center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_height = int(screen_height/3)
window_width = int(screen_width/3)

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



pad_x=5
pad_y=5

list_frame=LabelFrame(root,padx=pad_x,pady=pad_y,text='Status',font=base_font)
list_frame.grid(row=0,padx=pad_x,pady=pad_y,sticky='nsew')
list_frame.rowconfigure(index=0,weight=1)
list_frame.columnconfigure(index=0,weight=1)
main_box=Listbox(list_frame,font=main_box_font)
main_box.grid(row=0,column=0,padx=pad_x,pady=pad_y,sticky='nsew')

main_box.insert(END,"")
main_box.insert(END,"")
main_box.insert(END,"")
main_box.insert(END,"     This is a Gif!")

button_frame=LabelFrame(root,padx=pad_x,pady=pad_y,text='Operations',font=base_font)
button_frame.grid(row=1,padx=pad_x,pady=pad_y,sticky='nsew')

button_frame.columnconfigure(index=0,weight=1)
button_frame.columnconfigure(index=1,weight=1)
button_frame.columnconfigure(index=2,weight=1)



def delete():
    start=timeit.default_timer()
    
    organize=Organize()
    main_box.delete(0,END)
    
    folders=organize.count_folders()
    files=organize.count_files()

    
    main_box.insert(END,f' Number of Folders : {folders}')
    main_box.insert(END,f' Number of Files : {files}')

    organize.delete_empty_folders()
    
    fail_remove_folders=Organize().count_folders()
    
    if folders==fail_remove_folders:
        txt=" No folder is removed"
    else:
        remain = folders - fail_remove_folders
        txt=f' {remain} folder(s) removed'
    main_box.insert(END,txt)
    
    end=timeit.default_timer()
    total_time=round(end-start,5)
    main_box.insert(END,f' Total time : {total_time} ms')


delete_button=Button(button_frame,padx=pad_x,pady=pad_y,text='Delete empty folders',font=base_font,command=delete)
delete_button.grid(row=0,column=0,sticky='nsew',padx=2,pady=2)

def org():
    start=timeit.default_timer()
    
    organize=Organize()
    main_box.delete(0,END)
    
    folders=organize.count_folders()
    files=organize.count_files()

    
    main_box.insert(END,f' Number of Folders : {folders}')
    main_box.insert(END,f' Number of Files : {files}')
    
    organize.move()
    fail_move_files=Organize().count_files()
    if files==0:
        txt=" There's no file to be moved"
    elif fail_move_files == 0:
        txt= ' All files successfully moved'
    else:
        moved_files=files - fail_move_files
        txt = f' Unfortunately {moved_files} files moved, {fail_move_files} files failed'
    
    main_box.insert(END,txt)
    
    end=timeit.default_timer()
    total_time=round(end-start,5)
    main_box.insert(END,f' Total time : {total_time} ms')

org_button=Button(button_frame,padx=pad_x,pady=pad_y,text='Organize files',font=base_font,command=org)
org_button.grid(row=0,column=1,sticky='nsew',padx=2,pady=2)


def ExitApplication():
    MsgBox =messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()
        
ext_button=Button(button_frame,padx=pad_x,pady=pad_y,text='Exit',font=base_font,command=ExitApplication,bg='brown',fg='white')
ext_button.grid(row=0,column=2,sticky='nsew',padx=2,pady=2)

root.protocol("WM_DELETE_WINDOW", ExitApplication)

root.mainloop()