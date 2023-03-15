import tkinter as tk
from PIL import Image,ImageTk
    



root = tk.Tk()
frame = tk.Frame(root,bg="black")
frame.pack(pady=10)
root.config(bg="GREEN")
root.title("QR BASED ATTENDANCE SOFTWARE")

canvas= tk.Canvas(root, width= 600, height= 400)
canvas.pack(pady=10)
#Load an image in the script
img= ImageTk.PhotoImage(Image.open("download.png"))

#Add image to the Canvas Items
canvas.create_image(100,150,image=img)


l1 = tk.Label(frame, text="ATTENEDANZE SYSTEM",font=('Times', 24))
l1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)


l2 = tk.Label(frame2, text="USERNAME",font=('Times', 15))
l2.pack()


entry= tk.Entry(frame2, width= 40)
entry.focus_set()
entry.pack()
l2 = tk.Label(frame2, text="PASSWORD",font=('Times', 15))
l2.pack()

entry2= tk.Entry(frame2, width= 40)
entry2.focus_set()
entry2.pack()

btn= tk.Button(root, width= 40,text="Submit",bg="grey",fg="black")

btn.pack()
b2 = tk.Button(root,text="Click to create Account",font=('Times', 15),bg="grey")
b2.pack()





root.mainloop()
