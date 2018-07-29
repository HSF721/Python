
#coding=utf-8

import Tkinter

root = Tkinter.Tk()
varName = Tkinter.StringVar()
varName.set('')
varPwd = Tkinter.StringVar()
varPwd.set('')

labelName = Tkinter.Label(root, text='User Name:', justify=Tkinter.RIGHT, width=80)

labelName.place(x=10, y=5, width=80, height=20)

entryName = Tkinter.Entry(root, width=80,textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)
labelPwd = Tkinter.Label(root, text='Password:', justify=Tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

entryPwd = Tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

def login():

	name = entryName.get()
	pwd = entryPwd.get()
	print(name)
	print(pwd)
	if name=='admin'and pwd=='123456':
		print("success")
	else:
		print("fail")

	

def cancel():

	varName.set('')
	varPwd.set('')

buttonCancel = Tkinter.Button(root, text='取消', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)
buttonOk = Tkinter.Button(root, text='登录', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)
root.mainloop()