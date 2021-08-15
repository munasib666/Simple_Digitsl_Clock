from tkinter import *
import time

def times():
    current_time = time.strftime("%I:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)

root = Tk()
root.geometry("500x250")
clock = Label(root, font=("times", 55, "bold"), bg="black", fg='white')
clock.grid(row=2, column=2, pady=30, padx=100)
times()
digital = Label(root, text="Digital clock", font="times 15", fg="black")
digital.grid(row=0, column=2)
note = Label(root, text="hours  :  minutes  :  seconds   ", font="times 13 bold")
note.grid(row=3, column=2)
root.mainloop()