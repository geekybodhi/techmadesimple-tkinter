## Code based on vegaseat's "Updated Tint Tkinter Calculator" at DaniWeb
## Original at https://www.daniweb.com/programming/software-development/code/467452/updated-tiny-tkinter-calculator-python


# avoid integer division by Python2
from __future__ import division
from math import *
from functools import partial
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Advanced Demo Calculator")
        self.geometry("350x170+550+150")
        self.memory = 0
        self.create_widgets()
    
    def create_widgets(self):
        btn_list = [
        '7',  '8',  '9',  '*',  'C',
        '4',  '5',  '6',  '/',  'Mem >',
        '1',  '2',  '3',  '-',  '> Mem',
        '0',  '.',  '=',  '+',  'Neg', 
        'sqrt', 'nl', 'sin', 'cos', 'tan' ]

        r = 1
        c = 0
        for label in btn_list:
            tk.Button(self, text=label, width=5, relief='ridge', command=partial(self.calculate, label)).grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

        self.entry = tk.Entry(self, width=30, bg="green")
        self.entry.grid(row=0, column=0, columnspan=5)

    def calculate(self, key):
        if key == '=':
            if '_' in self.entry.get():
               self.entry.insert(tk.END, "Nice try, schmuck! Stick to calculations.")
            result = eval(self.entry.get())
            self.entry.insert(tk.END, " = " + str(result))
        elif key == 'C':
            self.entry.delete(0, tk.END)  
        elif key == '> Mem':
            self.memory = self.entry.get()
            if '=' in self.memory:
                val = self.memory.find('=')
                self.memory = self.memory[val+2:]
            self.title('Memory =' + self.memory)
        elif key == 'Mem >':
            self.entry.insert(tk.END, self.memory)
        elif key == 'Neg':
            if '=' in self.entry.get():
                self.entry.delete(0, tk.END)
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        elif key == 'sqrt':
            result = sqrt(eval(self.entry.get()))
            self.entry.insert(tk.END,"sqrt= "+str(result))
        elif key == 'nl':
            result = log(eval(self.entry.get()))
            self.entry.insert(tk.END,"natural log= "+str(result))
        elif key == 'sin':
            result = sin(eval(self.entry.get()))
            self.entry.insert(tk.END,"sin= "+str(result))
        elif key == 'cos':
            result = cos(eval(self.entry.get()))
            self.entry.insert(tk.END,"cos= "+str(result))
        elif key == 'tan':
            result = tan(eval(self.entry.get()))
            self.entry.insert(tk.END,"tan= "+str(result))
        else:
            if '=' in self.entry.get():
                self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, key)

app = Calculator()
app.mainloop()
