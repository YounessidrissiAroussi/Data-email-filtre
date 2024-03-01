from tkinter import *
from tkinter import filedialog 
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def filter_emails_by_domain(file_path, domain):
    filtered_data = []
    with open(file_path, 'r') as file:
        for line in file:
            if domain in line:
                filtered_data.append(line.strip())
    return filtered_data

def append_emails_to_file(data, file_path):
    with open(file_path, 'a') as file:
        for line in data:
            file.write(line + '\n')

def filter_domain(file_path, folder_name, progress_window):
    with open(file_path, 'r') as file:
        total_lines = sum(1 for line in file)
        file.seek(0)  # Reset file pointer to beginning
        for i, line in enumerate(file, 1):
            email = line.strip()
            index = email.index("@")
            domain = email[index+1:-4]
            filtered_data = filter_emails_by_domain(file_path, domain)
            create_folder = folder_name
            os.makedirs(create_folder ,exist_ok='True')
            append_emails_to_file(filtered_data, f"./{create_folder}/{domain}.txt")
            progress_var.set((i / total_lines) * 100)  # Update progress
            progress_window.update()  # Force update the GUI

def Generate():
    if filename != "":
        folder_window = tk.Toplevel(window)
        folder_window.geometry("300x150")
        folder_window.title("Folder Name")
        folder_window.iconbitmap("images/pngegg.ico")
        folder_window.configure(bg = "#282a49")
        
        folder_label = Label(folder_window, text="Enter Folder Name:", bg="#282a49", fg="white")
        folder_label.pack(pady=5)
        
        folder_entry = Entry(folder_window,  bd = 0,bg = "#f1f5ff", highlightthickness = 0)
        folder_entry.pack(pady=5)
       
        def start_processing():
            folder_name = folder_entry.get()
            if folder_name == "":
                tk.messagebox.showwarning("Warning", "Please enter a folder name.")
                return
            folder_window.destroy()
            progress_window = tk.Toplevel(window)
            progress_window.geometry("300x100")
            progress_window.title("Progress")
            progress_window.iconbitmap("images/pngegg.ico")
            progress_window.configure(bg = "#282a49")

            progress_label = Label(progress_window, text="Processing...", bg="#282a49", fg="white")
            progress_label.pack(pady=10)

            progress_bar = ttk.Progressbar(progress_window, mode='determinate', variable=progress_var)
            progress_bar.pack(pady=5)

            progress_bar.start()
            window.update()  # Force update the GUI
            filter_domain(filename, folder_name, progress_window)
            progress_bar.stop()
            progress_window.destroy()
            tk.messagebox.showinfo('Return','Files are done')
        
        start_button = Button(folder_window, text="Create", command=start_processing)
        start_button.pack(pady=5)

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
    command = Generate,
    relief = "flat")

b0.place(
    x = 561, y = 323,
    width = 180,
    height = 55
)

canvas.create_text(
    647.0, 126.5,
    text = "Enter Your File.",
    fill = "#515486",
    font = ("MontserratRoman-SemiBold", int(30.0))
)

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
    highlightthickness = 0
)

def path_filename():
    global filename
    filename = filedialog.askopenfilename()
    entry0.place(
        x = 494.0, y = 199,
        width = 321.0,
        height = 59)
    entry0.insert(0,filename)
        
img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = path_filename,
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

# Create progress bar
progress_var = DoubleVar()

window.resizable(False, False)
window.mainloop()
