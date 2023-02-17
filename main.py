import tkinter as tk
from tkinter import filedialog
import playfair
import binascii
def select_files():
    global filePath_list
    select_files_path = filedialog.askopenfilenames(filetypes=[("All","*.*")])
    select_files_path = mw.tk.splitlist(select_files_path)
    filePath_list = select_files_path
    fileINFOisFull()
def select_PassKeyfile():
    global passKey
    select_file_path = filedialog.askopenfilename()
    passKey = select_file_path
    fileINFOisFull()
def fileINFOisFull():
    global filePath_list
    global passKey
    if not filePath_list or not passKey:
        encryButton.config(state=tk.DISABLED)
        decryButton.config(state=tk.DISABLED)
    if filePath_list and passKey:
        encryButton.config(state=tk.ACTIVE)
        decryButton.config(state=tk.ACTIVE)
def readFilehex(path:str):
    f = open(path,'rb')
    hex_list = list(("{:02X}".format(int(c)) for c in f.read()))
    f.close()
    return ''.join(hex_list)
def encryFile():
    global filePath_list
    global passKey
    passKeyHex = readFilehex(passKey)
    for file in filePath_list:
        fileHex = readFilehex(file)
        cipherHex = playfair.encry(word=fileHex, passkey=passKeyHex)
        saveFile(file,cipherHex)
def decryFile():
    global filePath_list
    global passKey
    passKeyHex = readFilehex(passKey)
    for file in filePath_list:
        fileHex = readFilehex(file)
        cipherHex = playfair.decry(cipher=fileHex, passkey=passKeyHex)
        saveFile(file,cipherHex)

def saveFile(path:str,hex:str):
    f = open(path,'wb')
    hex = binascii.a2b_hex(hex)
    f.write(hex)
    f.close
if __name__ == '__main__':
    filePath_list = ()
    passKey = None;
    mw = tk.Tk()
    mw.title("16进制普莱费尔加密")
    mw.geometry('370x160')
    mw.resizable(False,False)

    tk.Label(mw,text="选择加/解密的文件").place(x=5,y=5)
    fileButton = tk.Button(mw,text="选择文件(可多选)",relief=tk.GROOVE)
    fileButton.config(width=50)
    fileButton.config(command=select_files)
    fileButton.place(x=5,y=25)


    tk.Label(mw,text="选择密钥文件").place(x=5,y=55)
    passkeyButton = tk.Button(mw,text="选择文件",relief=tk.GROOVE)
    passkeyButton.config(width=50)
    passkeyButton.config(command=select_PassKeyfile)
    passkeyButton.place(x=5,y=75)
    

    encryButton = tk.Button(mw,text="加密文件",relief=tk.GROOVE)
    encryButton.config(width=20)
    encryButton.config(command=encryFile)
    encryButton.place(x=5,y=125)

    decryButton = tk.Button(mw,text="解密文件",relief=tk.GROOVE)
    decryButton.config(width=20)
    decryButton.config(command=decryFile)
    decryButton.place(x=215,y=125)

    fileINFOisFull()
    mw.mainloop()