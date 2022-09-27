from tkinter import *
from tkinter import filedialog 
import json
import re

def Convert():
    pass

window = Tk()
window.geometry("862x519")
window.title("RUNKING")
window.iconbitmap("images/pngegg.ico")
window.configure(bg = "#282a49")
canvas = Canvas(
    window,
    bg = "#282a49",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    431, 0, 431+431, 0+519,
    fill = "#fcfcfc",
    outline = "")

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Convert,
    relief = "flat")

b0.place(
    x = 561, y = 323,
    width = 180,
    height = 55)

canvas.create_text(
    647.0, 126.5,
    text = "Enter Your File.",
    fill = "#515486",
    font = ("MontserratRoman-SemiBold", int(30.0)))

canvas.create_text(
    215.0, 215.5,
    text = "Welcome Runking",
    fill = "#fcfcfc",
    font = ("MontserratRoman-SemiBold", int(24.0)))

entry0_img = PhotoImage(file = f"images/img_textBox0.png")
entry0_bg = canvas.create_image(
    654.5, 229.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

def file():
    filename = filedialog.askopenfilename()
    if filename:
        entry0.place(
            x = 494.0, y = 199,
            width = 321.0,
            height = 59)
        entry0.insert(0,filename)
        file_txt = str(filename)
        data1 = []
        data2 = [] 
        file1 = "file22.json"
        with open(file_txt) as f:
            lines = f.readlines()
        # python_dict = {"dmain": lines} 
        # json_obj = json.dumps(python_dict)
        print(lines)
        for i in lines:
            domain = re.search("@[\w.]+", i)
            # print(domain.group())
            
        for x in lines:
                if domain.group() in x:
                    data1.append(lines)
        print(data1)
        
            
            
            
            
        
               
            
            

            
            
            
                    
           
            
                
                    

            
                     
                 
                   
            
                
                
            
               
                
                
            
                
                
                         
            

     
            


img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = file,
    relief = "flat")

b1.place(
    x = 785, y = 219,
    width = 24,
    height = 22)

canvas.create_text(
    215.0, 251.5,
    text = "For Filtered Data E-mail",
    fill = "#fcfcfc",
    font = ("MontserratRoman-SemiBold", int(24.0)))

window.resizable(False, False)
window.mainloop()
