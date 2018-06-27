from tkinter import *


def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def ClearFunc():
    global operator
    operator = ''
    text_input.set('')

def equalto():
    global operator
    result = str(eval(operator))
    text_input.set(result)
    operator = ''


cal = Tk()
cal.title("Calculator")
operator =''
text_input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable = text_input, bd=30, insertwidth=4,
                   bg="powder blue", justify = 'right').grid(columnspan = 4)

btn7 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='7', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='9', command=lambda:btnClick(9)).grid(row=1, column=2)
add = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='+', command=lambda:btnClick('+')).grid(row=1, column=3)
btn4 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='6',command=lambda:btnClick(6)).grid(row=2, column=2)
sub = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='-', command=lambda:btnClick('-')).grid(row=2, column=3)
btn1 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='3', command=lambda:btnClick(3)).grid(row=3, column=2)
mul = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='*', command=lambda:btnClick('*')).grid(row=3, column=3)
btn0 = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='0', command=lambda : btnClick(0)).grid(row=4, column=0)
Clear = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='C', command=ClearFunc).grid(row=4, column=1)
equalto = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='=',command=equalto).grid(row=4, column=2)
div = Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
              text='/', command=lambda:btnClick('/')).grid(row=4, column=3)

cal.mainloop()