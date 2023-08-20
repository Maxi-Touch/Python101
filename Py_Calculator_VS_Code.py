from tkinter import *
import math
from unittest import result

root = Tk()
blank_space = " "
root.title(blank_space + "Agrotek Calculator")
root.resizable(width=False, height=False)
root.geometry("315x500+460+40")

coverFrame = Frame (root, bd=0, pady=0, bg='silver',)
coverFrame.grid()

CoverMainFrame = Frame(coverFrame, bd=0, pady=0)
CoverMainFrame.grid()

MainFrame = Frame(CoverMainFrame, bd=0, bg='silver', pady=90)
MainFrame.grid()

class Calculator():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value= True
        self.check_sum = False
        self.op=""
        self.result=False
        
    def numberEnter(self,num):
        self.result=False
        firstnum=entDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum==".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
        
    def display(self,value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)
    
    def backspace(self):
        numLen = len(entDisplay.get())
        entDisplay.delete(numLen - 1, 'end')
        if numLen==1:
            entDisplay.insert(0, "0")
            
    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
        
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(entDisplay.get())
    
    def valid_function(self):
        if self.op=="add":
            self.total += self.current
        if self.op=="sub":
            self.total -= self.current
        if self.op=="multi":
            self.total *= self.current
        if self.op=="divide":
            self.total /= self.current
        if self.op=="mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
        
    def operation(self, op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
        self.check_sum=True
        self.op = op
        self.result=False
        
    def mathsPM(self):
        self.result=False
        self.current = -(float(entDisplay.get()))
        self.display(self.current)
        
    def squared(self):
        self.result=False
        self.current=math.sqrt(float(entDisplay.get()))
        self.display(self.current)
        
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
    
added_value = Calculator()
entDisplay = Entry(MainFrame, font=('arial', 18, 'bold'), bd=0, width=24,  bg='silver', justify=RIGHT)
entDisplay.grid(row=0, column=0, columnspan=4, pady=15)
entDisplay.insert(0, "0")

numpad="789456123"
i=0
btn=[]

for j in range(3,6):
    for k in range(3):
        btn.append(Button(MainFrame, width=5, height=1, font=('Calibri', 20, 'bold'), bd=0, bg='White', text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"]=lambda x=numpad[i]: added_value.numberEnter(x)
        i += 1
btnClearAll=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text=chr(67)+chr(69), command=added_value.all_Clear_Entry)
btnClearAll.grid(row=2, column=0, pady=1)

btnClear=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text=chr(67), command=added_value.Clear_Entry)
btnClear.grid(row=2, column=1, pady=1)

btnBackSpace=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="←" , command=added_value.backspace)
btnBackSpace.grid(row=2, column=2, pady=1)

btnPM=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text=chr(247), command=lambda:added_value.operation("divide"))
btnPM.grid(row=2, column=3, pady=1)

btnPercent=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="%")
btnPercent.grid(row=1, column=0, pady=1)

btnSqr=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="×", command=added_value.squared)
btnSqr.grid(row=1, column=1, pady=1)

btnSq=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="×")
btnSq.grid(row=1, column=2, pady=1)

btnX=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="×")
btnX.grid(row=1, column=3, pady=1)

btnMutiply=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver',text="*" , command=lambda:added_value.operation("multi"))
btnMutiply.grid(row=3, column=3, pady=1)

btnMinu=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver',text="-" , command=lambda:added_value.operation("sub"))
btnMinu.grid(row=4, column=3, pady=1)

btnPlus=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver',text="+" , command=lambda:added_value.operation("add"))
btnPlus.grid(row=5, column=3, pady=1)

btnPlusMinu=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver',text=chr(177), command=added_value.mathsPM)
btnPlusMinu.grid(row=6, column=0, pady=1)

btnZero=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=0, bg='white', text="0", command=lambda:added_value.numberEnter(0))
btnZero.grid(row=6, column=1, pady=1)

btnDot=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text=".", command=lambda:added_value.numberEnter("."))
btnDot.grid(row=6, column=2, pady=1)

btnEqual=Button(MainFrame, width=5, height=1, font=('Calibri', 20), bd=1, bg='silver', text="=",  command=added_value.sum_of_total)
btnEqual.grid(row=6, column=3, pady=1)

root.mainloop()


