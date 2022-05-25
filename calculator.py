import re
from tkinter import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title('calculator')

        self.num1=0

        self.display = Entry(self.root,font=('Arial','14'),width =15 )
        self.display.grid(row = 0, column =0)
#first key rows
        self.frame1 = Frame(self.root,padx=10)
        self.frame1.grid(row =1,column =0)

        self.btn7 = Button(self.frame1,text='7', padx=10,pady=5,command=lambda:self.on_key_click(7))     
        self.btn7.grid(row=0,column=0)
        
        self.btn8 = Button(self.frame1,text='8', padx=10,pady=5)     
        self.btn8.grid(row=0,column=1)

        self.btn9 = Button(self.frame1,text='9', padx=10,pady=5)     
        self.btn9.grid(row=0,column=2)
        
        

#second key rows
        self.frame2 = Frame(self.root,padx=10)
        self.frame2.grid(row =1,column =0)

        self.btn4 = Button(self.frame1,text='4', padx=10,pady=5,command=lambda:self.on_key_click(4))     
        self.btn4.grid(row=0,column=0)
        
        self.btn5 = Button(self.frame1,text='5', padx=10,pady=5,command=lambda:self.on_key_click(5))     
        self.btn5.grid(row=0,column=1)

        self.btn6 = Button(self.frame1,text='6', padx=10,pady=5,command=lambda:self.on_key_click(6))     
        self.btn6.grid(row=0,column=2)

        self.root.mainloop()

    def on_key_click(self,val):
        if val =='c':
            self.display.delete(0,END)

        elif val=='+' or val =='-'or val == '/' or val =='*':
            self.num1 = float(self.display.get())
            self.op = val
            print(self.num1,self.op)
        elif val== '=':
            self.num2=float(self.display.get())
            print(self.num2)
            self.display.delete(0,END)
            self.display.insert(0,self.calculate())

            
        else:
             if val==0:
                 if self.display.get() != '':
                    self.display.insert(END,  val)
                 else:
                     self.display.insert(END,  val)

                
        def calculate(self):
            if self.op == '+':
                return self.num1+self.num2
            elif self.op == '-':
                return self.num1-self.num2
            









#dot(.) backspace, +/-, sqrt



c= Calculator()