from tkinter import *

root = Tk()

class Calculator:
    
    def iniLabel(self, row, col, text, sticky, padding):
            self.row = row
            self.column = col
            self.sticky = sticky
            self.pady = padding

            self.labels[self.label_order.index(text)] = Label(self.label_fkey, bg="grey")
            self.labels[self.label_order.index(text)].grid(row = row, column = col, sticky = sticky, pady = padding)
            self.buttons[self.label_order.index(text)] = Button(self.labels[self.label_order.index(text)], text = text, font=("Verdana", "18"), height=1, width=8,command= lambda: self.onClickButton(text),bg="grey",fg="yellow")
            self.buttons[self.label_order.index(text)].pack()

    def onClickButton(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""

    def onClickEvaluate(self):
        try:
            self.answer = eval(self.entry.get())
            self.var.set(self.answer)
            self.operator = str(self.answer)
        except ZeroDivisionError:
            print("You cannot divide by Zero")
        except:
            print("Please input an entire calculation! Strings are not allowed.")

    def __init__(self, master):

        self.operator = ""
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=45 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg="black", fg = "white" ,width=69,bd=36,insertwidth=4,justify="right",font=("arial",10,"bold"))
        self.entry.pack()
        self.t = Text(self.entry,height=40)
        self.labels = ["0"] * 19
        self.buttons = ["0"] * 19
        
        self.label_order = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "+", "(", "0",  ")",  "." ]
        self.count_row = 1
        self.count_column = 0
        self.count_sticky = 0
        self.sticky = ["W", "E"]


        self.label_fkey = Label(root, height=15, width=15, bg="gray30")
        self.label_fkey.pack(fill=BOTH, expand=True)

        for label in self.label_order:
                
            if self.count_column >= 4:
                self.count_column = 0
                self.count_row += 1
            if self.count_sticky % 2 == 0:
                self.count_sticky = 0
            
            self.iniLabel(self.count_row, self.count_column, label, self.sticky[self.count_sticky], 3)
            self.count_column += 1
        
        lb_clear = Label(self.label_fkey, bg="grey")
        lb_clear.grid(row=0, column=0,columnspan=2)
        bt_clear = Button(lb_clear, text="C", font=("Verdana", "18"), height=1, width=18,command = self.clear,bg="grey",fg="yellow")
        bt_clear.pack()

        lb_eq = Label(self.label_fkey, bg="grey")
        lb_eq.grid(row=0, column=2)
        bt_eq = Button(lb_eq, text="=", font=("Verdana", "18"), height=1, width=8, command = self.onClickEvaluate, bg="grey",fg="yellow")
        bt_eq.pack()

        lb_minus = Label(self.label_fkey, bg="grey")
        lb_minus.grid(row=0, column=3)
        bt_minus = Button(lb_minus, text="-", font=("Verdana", "18"), height=1, width=8,command = lambda: self.onClickButton("-"),bg="grey",fg="yellow")
        bt_minus.pack()

        

       
def main():
    c = Calculator(root)
    root.title("Oujian\"s Calculator")
    root.mainloop()

if __name__ == "__main__":
    main()
