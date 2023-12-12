from tkinter import *
import time

keys = [['1','2','3','4','5','6','7','8','9','0'],['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['@','-','z','x','c','v','b','n','m','_','.'],['@outlook.com','@hotmail.com','@gmail.com',"<-"]]

button_list = [[]]
keyboardWidth = 750
keyboardHeight = 300
rowHeight = keyboardHeight // len(keys)

win = Tk()
win.attributes('-fullscreen',True) 
rowIndex = 0
keyIndex = 0
email = ""
xOffset = 10
yOffset = 150

def GetButton(button):
    global email
    char = button.cget("text")
    if char != "<-":
        email = email + button.cget("text")
    else:
        if len(email) > 0:
            email = email.rstrip(email[-1])
    labelEmail.config(text = email)

def ClearAllWidgets(window):
    for widget in window.winfo_children():
        widget.place_forget()

def SendButton(window):
    print("Send button pressed")
    ClearAllWidgets(window)
    


labelEmail = Label(win,text = "  enter email  ",font=("Arial",26))
labelEmail.place(x=20, y=50)
buttonSend = Button(win,text="Send", font=("Arial",26),command= lambda:SendButton(win))
buttonSend.place(x=650, y=50)

for rowIndex, row in enumerate(keys):
    keysWidth = keyboardWidth // len(row)

    for keyIndex, key in enumerate(row):
        button = Button(win,text = keys[rowIndex][keyIndex])
        button.config(command=lambda button=button: GetButton(button))
        button.place(width = keysWidth, height = rowHeight,x=(xOffset+keysWidth * keyIndex),y=(yOffset + rowHeight * rowIndex))
        button_list.append(button)
    button_list.append([])


while True:
    win.update()
