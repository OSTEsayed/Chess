import tkinter as tk
import time

class Clock():
    def __init__(self):
        self.now=10
        self.later =50
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.now =self.now-1
        if self.now==0:
            self.later =self.later-1
            self.now=10

        self.label.configure(text="{}:{}".format(self.later,self.now))
        self.root.after(1000, self.update_clock)

app=Clock()