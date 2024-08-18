import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar 
from pydub import AudioSegment
from tkinter import messagebox
import segno

root = tk.Tk()



root.title("Video to Audio Converter")
root.geometry("1350x450")
root.resizable(width=False, height=False)
root.configure(background="#FFFFFF")
data=StringVar()
filepath2=""



def browse_input_command():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Select video file", filetypes=(("Video files", "*.mp4"),("All files","*.*")))
    
    
    input_file_path_label.config(text=file_path)


def browse_output_command():
    global output_path
    output_path = filedialog.asksaveasfilename(initialdir="/", title="Save audio file as", filetypes=(("Audio files", "*.mp3"),("All files","*.*")))
    
    
    output_file_path_label.config(text=output_path)


def convert_command():
    if not file_path or not output_path:
        messagebox.showerror("Error", "Please select both input and output paths.")
        return

    try:
        
        video = AudioSegment.from_file(file_path)
        video.export(output_path, format="mp3")

       
        messagebox.showinfo("Success", "Video converted to Audio successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    
def outputcommand():
    global filepath2
    filepath2 = filedialog.asksaveasfilename(initialdir="/", title="Save Barcode ", filetypes=(("Barcode", "*.png"),("All files","*.*")))
    SIDE_BUTTONLABEL1.config(text = filepath2)
    
     


def fn():
    global data
    global qrcode
    global filepath2

    input_data =data.get()
    if not filepath2:
        messagebox.showerror("Error", "Please choose an output path for the QR code.")
    else:
        
        if not filepath2.lower().endswith(".png"):
            filepath2 += ".png"
    
    qrcode=segno.make_qr(input_data)
    qrcode.save(filepath2,scale = 5)
    messagebox.showinfo("Success","Link coverted to Barcode")
     
    


title_label = tk.Label(root)
title_label.configure(background="#FF7200", foreground="#000000", font="Arial 20 bold", justify="center", text="Video to Audio Converter")
title_label.place(x=0, y=0, width=675, height=50,)

browse_input_button = tk.Button(root,bg="cyan")
browse_input_button.configure(font="Arial 14",justify="center", text="Browse Input", command=browse_input_command)
browse_input_button.place(x=30, y=80, width=160, height=40)

input_file_path_label = tk.Label(root)
input_file_path_label.configure(background="#333333", foreground="#FFFFFF", font="Arial 14", justify="center", text="Input File Path")
input_file_path_label.place(x=220, y=80, width=400, height=40)

browse_output_button = tk.Button(root,bg="cyan")
browse_output_button.configure(font="Arial 14", justify="center", text="Output Path ", command=browse_output_command)
browse_output_button.place(x=30, y=150, width=160, height=40)

output_file_path_label = tk.Label(root)
output_file_path_label.configure(background="#333333", foreground="#FFFFFF", font="Arial 14", justify="center", text="Output File Path")
output_file_path_label.place(x=220, y=150, width=400, height=40)

convert_button = tk.Button(root,bg="yellow")
convert_button.configure(font="Arial 14", justify="center", text="Convert", command=convert_command)
convert_button.place(x=180, y=250, width=300, height=40)

SIDE_BORDER =tk.Frame(root,bg="#000000")
SIDE_BORDER.configure(height=1000,width=2)
SIDE_BORDER.pack()

SIDE_LABEL=tk.Label(root)
SIDE_LABEL.configure(text="Qr Code Generator" ,background="#FF7200",foreground="#000000",font=("Arial 20 bold"))
SIDE_LABEL.place(x=676,y=0,height=50,width=675)

SIDE_BUTTON =tk.Button(root,bg="cyan")
SIDE_BUTTON.configure(text = "Enter a link " , font=("Arial 14"))
SIDE_BUTTON.place(x=700,y=80,height=40,width=160)

SIDE_BUTTON1 =tk.Button(root,bg="cyan")
SIDE_BUTTON1.configure(text = "Output Path " , font=("Arial 14"),command =outputcommand)
SIDE_BUTTON1.place(x=700,y=150,height=40,width=160)

SIDE_BUTTONLABEL1=tk.Label(root)
SIDE_BUTTONLABEL1.configure(text = "Output File Path", font= "Arial 14",background ="#333333",foreground="#FFFFFF")
SIDE_BUTTONLABEL1.place(x=900,y=150,width=400,height=40)


SIDE_BUTTONLABEL=tk.Entry(root,textvariable= data)
SIDE_BUTTONLABEL.place(x=900,y=80,width=400,height=40)


CONVERT_BUTTON = tk.Button(root,bg="yellow")
CONVERT_BUTTON.configure(font="Arial 14", justify="center", text="Convert", command=fn)
CONVERT_BUTTON.place(x=850, y=250, width=300, height=40)


root.mainloop()

