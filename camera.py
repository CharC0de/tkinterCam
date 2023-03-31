import tkinter as tk
import cv2
from PIL import Image, ImageTk

import bcrypt

# Create a tkinter window
root = tk.Tk()
root.title("Camera Viewer")
# root.geometry()

# Create a label to display the camera feed

title = tk.Label(root, text="Login Window", font="Arial 20 bold",)

userlbl = tk.Label(root,text="Username", font="Arial 13")
passlbl = tk.Label(root,text="Password", font="Arial 13")
userEntry = tk.Entry(root)
passEntry = tk.Entry(root, show="*")
loginButton = tk.Button(root, text="Login")
exitButton = tk.Button(root, text="Exit")

cap = cv2.VideoCapture(0)
label = tk.Label(root)

label.grid(column=0,row=1, rowspan=2, columnspan=1) 
title.grid(column=0,row=0, sticky="NSEW")
userlbl.grid(column=1,row=1, sticky="EW")
passlbl.grid(column=1,row=2, sticky="EW")
userEntry.grid(column=2,row=1, sticky="E")
passEntry.grid(column=2,row=2, sticky="E")
loginButton.grid(column=1,row=3, sticky="NSEW")
exitButton.grid(column=2,row=3, sticky="NSEW")

def update_camera():
    ret, frame = cap.read()
    if ret:
        # Convert the OpenCV frame to a PIL image
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(image=img)
        label.img_tk = img_tk  # keep a reference to prevent garbage collection
        label.config(image=img_tk)
    root.after(10, update_camera)  # update every 10 milliseconds
update_camera()

# Start updating the camera feed in the tkinter window
def capture_frame():
    ret, frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(image=img)
        label.img_tk = img_tk  # keep a reference to prevent garbage collection
        label.config(image=img_tk)
# Start the tkinter main loop


     
        
def infoScreen():
    child = tk.Toplevel(root)
    imglbl=tk.Label(child)
    def capture_frame():
        ret, frame = cap.read()
        if ret:
            # Save the captured frame to a file
            filename = "captured_frame.jpg"
            cv2.imwrite(filename, frame)
            
            # Do something with the captured frame, such as display it in a label
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(image=img)
            imglbl.img_tk = img_tk  # keep a reference to prevent garbage collection
            imglbl.config(image=img_tk)
    capture_frame()
    title = tk.Label(child, text="Owner Info", font="Arial 20 bold",)
    namelbl = tk.Label(child,text="Name: Charles Reiner Egano", font="Arial 13")
    agelbl = tk.Label(child,text="Age: 21", font="Arial 13")
    addresslbl = tk.Label(child,text="Address: Barangay Gusa Cagayan de Oro City", font="Arial 13")
    courslbl = tk.Label(child,text="Course: Bachelor of Science in Information Technology", font="Arial 13")
    
    title.grid(column=0,row=0, sticky="NSEW")
    imglbl.grid(column=0,row=1,rowspan=4,sticky="NSEW")
    namelbl.grid(column=1,row=1)
    agelbl.grid(column=1,row=2)
    addresslbl.grid(column=1,row=3)
    courslbl.grid(column=1,row=4)
    
   
    
loginButton.config(command=infoScreen)
    
root.mainloop()

# Release the camera and close the tkinter window when done
cap.release()
cv2.destroyAllWindows()