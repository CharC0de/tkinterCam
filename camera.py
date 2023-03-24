import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create a tkinter window
root = tk.Tk()
root.title("Camera Viewer")

# Create a label to display the camera feed
label = tk.Label(root)
label.pack()

# Initialize the camera
cap = cv2.VideoCapture(0)

# Define a function to update the camera feed in the tkinter window
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

# Start updating the camera feed in the tkinter window
update_camera()

# Start the tkinter main loop
root.mainloop()

# Release the camera and close the tkinter window when done
cap.release()
cv2.destroyAllWindows()