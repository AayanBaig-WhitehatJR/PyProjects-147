# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 19:04:24 2021

@author: taru_
"""

from tkinter import *
root=Tk()
root.title("ASCII Code test")
root.geometry("400x400")
root.configure(bg="cyan4")

enter_text=Entry(root)
enter_text.place(relx=0.5, rely=0.2, anchor=CENTER)

ascii_label=Label(root, text="Text to ASCII: ", fg="LightSkyBlue1", bg="tomato2")
ascii_label.place(relx=0.5, rely=0.6, anchor=CENTER)

encrypted_text=Label(root, text="Encrypted Text: ", fg="LightSkyBlue1", bg="tomato2")
encrypted_text.place(relx=0.5, rely=0.8, anchor=CENTER)

def convertASCII():
    storetext=enter_text.get()
    for letter in storetext:
        ascii_label["text"]+=str(ord(letter))+" "
        ascii_int = int(ord(letter)) 
        encrypted_value = ascii_int-1
        encrypted_text["text"]+=chr(encrypted_value)
        

showASCIIval=Button(root, text="Show ASCII Code + Encrypted Value", fg="LightSkyBlue1", bg="tomato2", command=convertASCII)
showASCIIval.place(relx=0.5, rely=0.4, anchor=CENTER)

    
#end tkinter template to make it show
root.mainloop()