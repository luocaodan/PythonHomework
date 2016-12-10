#7-2.py
import tkinter
import tkinter.messagebox

'''
这个就照着样例改改就好了，就是一些参数
布局的话row表示行，column表示列，根据位置填数字就好了
'''
top = tkinter.Tk() #创建主窗体
def login(): #登录按钮事件响应函数
    if (UserEntry.get() == "admin" and PasswdEntry.get() == "123456"):
        tkinter.messagebox.showinfo('提示','登录成功')
    else:
        tkinter.messagebox.showinfo('提示','账号或密码错误')

def cancel():
    top.destroy()
label1 = tkinter.Label(top,text="UserName:")#创建UserName label
label1.grid(row=0,column=0)#设置布局
label2 = tkinter.Label(top,text="Password:")#创建Password Label
label2.grid(row=1,column=0)#设置布局
UserEntry = tkinter.Entry(top)#创建Entry UserName
UserEntry.grid(row=0,column=1)#设置布局
PasswdEntry = tkinter.Entry(top)#创建Password Entry
PasswdEntry.grid(row=1,column=1)
PasswdEntry['show'] = '*'#设置Password Entry的显示风格
button1 = tkinter.Button(top ,text='login',command=login)#创建button，并设置响应
button1.grid(row=2,column=0)

button2 = tkinter.Button(top ,text='cancel',command=cancel)#创建button，用于Cancel
button2.grid(row=2,column=1)
top.mainloop()
