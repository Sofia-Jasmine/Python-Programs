import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from tkinter import messagebox


root = tk.Tk()


root.title("Video to Audio Converter")
root.geometry("1000x400")
root.resizable(width=False, height=False)
root.configure(background="#00302C")

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


title_label = tk.Label(root)
title_label.configure(background="#FFFFFF", foreground="#000000", font="Arial 18 bold", justify="center", text="Video to Audio Converter")
title_label.place(x=0, y=0, width=1000, height=50)

browse_input_button = tk.Button(root)
browse_input_button.configure(font="Arial 14",justify="center", text="Browse Input", command=browse_input_command)
browse_input_button.place(x=30, y=80, width=160, height=40)

input_file_path_label = tk.Label(root)
input_file_path_label.configure(background="#3b4370", foreground="#ffffc5", font="Arial 14", justify="center", text="Input File Path")
input_file_path_label.place(x=220, y=80, width=750, height=40)

browse_output_button = tk.Button(root)
browse_output_button.configure(font="Arial 14", justify="center", text="Output Path ", command=browse_output_command)
browse_output_button.place(x=30, y=150, width=160, height=40)

output_file_path_label = tk.Label(root)
output_file_path_label.configure(background="#3b4370", foreground="#ffffc5", font="Arial 14", justify="center", text="Output File Path")
output_file_path_label.place(x=220, y=150, width=750, height=40)

convert_button = tk.Button(root)
convert_button.configure(font="Arial 14", justify="center", text="Convert", command=convert_command)
convert_button.place(x=320, y=290, width=350, height=40)




root.mainloop()
