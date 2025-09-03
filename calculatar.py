from tkinter import *
from unittest import result
first=second=operator=None
def get_digit(digit):
    curent=result_label['text']
    new = curent + str(digit)
    result_label.configure(text=new)
def get_operator(op):
    global first, operator
    first=int(result_label['text'])
    operator=op
    result_label.configure(text='')
def clear():
    result_label.configure(text='')
def get_result():
    global first,second, operator
    second = int(result_label['text'])
    if operator == '+':
        result_label.configure(text=str(first + second))
    elif operator == '-':
        result_label.configure(text=str(first - second))
    elif operator == '*':
        result_label.configure(text=str(first * second))
    else:
        if second == 0:
            result_label.configure(text='error')
        else:
            result_label.configure(text=str(round(first/second,2)))
from streamlit import button

root=Tk()
root.geometry("295x380")
root.resizable(0,0)
root.configure(bg='black')
result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=10,pady=(48,40),sticky='w')
result_label.configure(font=('verdana',20,'bold'))

btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.configure(font=('verdana',14,'bold'))

btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.configure(font=('verdana',14,'bold'))

btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.configure(font=('verdana',14,'bold'))

btnmul=Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btnmul.grid(row=1,column=3)
btnmul.configure(font=('verdana',14,'bold'))

btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.configure(font=('verdana',14,'bold'))
btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.configure(font=('verdana',14,'bold'))
btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.configure(font=('verdana',14,'bold'))
btnmin=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btnmin.grid(row=2,column=3)
btnmin.configure(font=('verdana',14,'bold'))

btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.configure(font=('verdana',14,'bold'))
btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.configure(font=('verdana',14,'bold'))
btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.configure(font=('verdana',14,'bold'))
btnadd=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('+') )
btnadd.grid(row=3,column=3)
btnadd.configure(font=('verdana',14,'bold'))

btnclc=Button(root,text='AC',bg='#00a65a',fg='white',width=5,height=2,command=lambda:clear())
btnclc.grid(row=4,column=0)
btnclc.configure(font=('verdana',14,'bold'))
btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.configure(font=('verdana',14,'bold'))
btnequal=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btnequal.grid(row=4,column=2)
btnequal.configure(font=('verdana',14,'bold'))
btndiv=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btndiv.grid(row=4,column=3)
btndiv.configure(font=('verdana',14,'bold'))
root.mainloop()