
#coding=utf-8
import os
import Tkinter as tk
window = tk.Tk()
window.title('XML Operation')
window.geometry('600x400')
 
l = tk.Label(window,text='OMG!this is TK!',bg='green',font=('Arial',12),width=15,
             height=2)
l.pack()   #安置
#l.place()

fileFathEntry = tk.Entry(window,width=50,bg="white",fg="black")
fileNameEntry = tk.Entry(window,width=50,bg="white",fg="black")
nodeFathEntry = tk.Entry(window,width=50,bg="white",fg="black")
nodeNameEntry = tk.Entry(window,width=50,bg="white",fg="black")
nodeValueEntry = tk.Entry(window,width=50,bg="white",fg="black")
#entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
fileFathEntry.pack()
fileNameEntry.pack()
nodeFathEntry.pack()
nodeNameEntry.pack()
nodeValueEntry.pack()


def ChangeNodeValue():
	#获取编辑框的值
	fileFath = fileFathEntry.get()
	fileName = fileNameEntry.get()
	nodeFath = nodeFathEntry.get()
	nodeValue = nodeValueEntry.get()

	rootPath = '.'
	for dirpath, dirnames, filenames in os.walk(rootPath):
		for filepath in filenames:
			print(filepath)
 			print (os.path.join(dirpath, filepath))
			print(fileFath)

def AddNodeValue():
	#获取编辑框的值
	fileFath = fileFathEntry.get()
	fileName = fileNameEntry.get()
	nodeFath = nodeFathEntry.get()
	nodeValue = nodeValueEntry.get()
	print(fileFath)

def DelNodeValue():
	#获取编辑框的值
	fileFath = fileFathEntry.get()
	fileName = fileNameEntry.get()
	nodeFath = nodeFathEntry.get()
	nodeValue = nodeValueEntry.get()
	print(fileFath)


tk.Button(window, text='更改节点值', command=ChangeNodeValue).pack()

tk.Button(window, text='增加节点', command=AddNodeValue).pack()

tk.Button(window, text='删除节点', command=DelNodeValue).pack()

window.mainloop() 