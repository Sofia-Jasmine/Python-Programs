def browse_input_command():
    global filepath
    file_path = filedialog. askopenfilename(intialdir="/", title"select video types", filetypes=(( "video files",".mp4"), ("All files","*.*")))
    browse_input_label.configuration(text=file_path)
def browse_output_command():
    global output_path
    output_path= filedialog.asksaveasfilename (initialdir="/",title"select audio files as", filetypes=(("audio files",".mp3"),("All files",,"*.*")))
    browse_output_label.configuration(text=output_path)
def convert_command():
    if not file_path or not output_path:
        messagebox. showerror("error","Please select both input and output paths.")
        return
    try:
        video=Audiosegment.from_file(file_path)
        video.export(output_path, format="mp3")
        messagebox.showerror("Error ",f"An error  occured : {str(e)}")
def outputcommand():
    global filepath2
    filepath2= filedialog.asksaveasfilename(initialdir="/",title="Save Barcode",filetypes=(("barcode",".png"),("All files","*.*")))
    side_buttonlabel1.configure(text=filepath2)
def convert_qr():
    global data
    global  qrcode
    global filepath2
    input_data=data.get()
    if not filepath2:
        messagebox.showerror("Error","Please choose an output path")
    else:
        if not filepath2.lower().endswith(".png"):
            filepath2+=".png"
    qrcode=segno.make_qr(input_data)
    qrcode.save(filepath2,scale =5)
    messagebax.showinfo("Success", "link converted into qrcode")
