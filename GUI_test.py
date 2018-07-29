
#coding=utf-8
import os
import Tkinter as tk
import re
window = tk.Tk()
window.title('XML Operation')
window.geometry('600x650')

strFilePath = tk.StringVar()
strFilePath.set('')
strfileName = tk.StringVar()
strfileName.set('')
strnodePath = tk.StringVar()
strnodePath.set('')
strnodeName = tk.StringVar()
strnodeName.set('')
strnodeValue = tk.StringVar()
strnodeValue.set('')

filePathEntry = tk.Entry(window,width=50,bg="white",fg="black", textvariable=strFilePath)
fileNameEntry = tk.Entry(window,width=50,bg="white",fg="black", textvariable=strfileName)
nodePathEntry = tk.Entry(window,width=50,bg="white",fg="black", textvariable=strnodePath)
nodeNameEntry = tk.Entry(window,width=50,bg="white",fg="black", textvariable=strnodeName)
nodeValueEntry = tk.Entry(window,width=50,bg="white",fg="black", textvariable=strnodeValue)
#entry1=tk.Entry(win,show="*",width=50,bg="red",fg="black")
filePathLable = tk.Label(window, width=20, text='文件路径:', justify=tk.RIGHT)
filePathLable.place(x=50, y=30)
filePathEntry.place(x=200, y=30)
fileNameLable = tk.Label(window, width=20, text='文件名称:', justify=tk.RIGHT)
fileNameLable.place(x=50, y=80)
fileNameEntry.place(x=200, y=80)
nodePathLable = tk.Label(window, width=20, text='节点路径:', justify=tk.RIGHT)
nodePathLable.place(x=50, y=130)
nodePathEntry.place(x=200, y=130)
nodeNameLable = tk.Label(window, width=20, text='新增节点名称:', justify=tk.RIGHT)
nodeNameLable.place(x=50, y=180)
nodeNameEntry.place(x=200, y=180)
nodeValueLable = tk.Label(window, width=20, text='新增/修改节点值:', justify=tk.RIGHT)
nodeValueLable.place(x=50, y=230)
nodeValueEntry.place(x=200, y=230)

operationRecordEntry = tk.Entry(window, bg="white",fg="black")
operationRecordEntry.place(x=70, y=270, width=480, height=300)

def ChangeNodeValue():
	#获取编辑框的值
	filePath = filePathEntry.get()
	fileName = fileNameEntry.get()
	nodePath = nodePathEntry.get()
	nodeValue = nodeValueEntry.get()

	rootPath = '.'
	for dirpath, dirnames, filenames in os.walk(rootPath):
		for filepath in filenames:
			print(filepath)
 			print (os.path.join(dirpath, filepath))
			print(filePath)

def AddNodeValue():
	#获取编辑框的值
	filePath = filePathEntry.get()
	fileName = fileNameEntry.get()
	nodePath = nodePathEntry.get()
	nodeValue = nodeValueEntry.get()
	print(nodePath)
	nodeNameList = re.split(r';', nodePath)


def DelNodeValue():
	#获取编辑框的值
	filePath = filePathEntry.get()
	fileName = fileNameEntry.get()
	nodePath = nodePathEntry.get()
	nodeValue = nodeValueEntry.get()
	print(filePath)

def DelOprationRecord():
	print('hello')

tk.Button(window, text='更改节点值', command=ChangeNodeValue).place(x=100, y=600)

tk.Button(window, text='增加节点', command=AddNodeValue).place(x=200, y=600)

tk.Button(window, text='删除节点', command=DelNodeValue).place(x=300, y=600)

tk.Button(window, text='清除操作记录', command=DelOprationRecord).place(x=400, y=600)

window.mainloop() 