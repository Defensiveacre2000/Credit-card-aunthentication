from tkinter import*
root = Tk()
root.title("Credit card aunthentication")
root.geometry("850x450")
root.configure(background = "yellow")
import random
from PIL import ImageTk , Image

credit_card = ImageTk.PhotoImage(Image.open("credit.jpg"))

pin_of_card = Entry(root , fg = "red")
pin_of_card.place(relx = 0.5 , rely = 0.2 , anchor = CENTER)

image_1 = Label(root)
image_1["Image"] = credit_card
image_1.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)


def authentication():
    try:
        input_value = int(pin_of_card.get())
        messagebox.showinfo("Alert" , "Credit card accepted")
        
    except(ValueError):
         messagebox.showinfo("Alert" , "Credit card not accepted. Please enter valid pin code")
         
         

button_1 = Button(root , text = "Check Credit Card" , bg = "blue" , command = aunthentication)
button_1.place(relx = 0.5 , rely = 0.35 , achor = CENTER)

root.mainloop()