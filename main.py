import tkinter

def hello():
    print("Hello world")
    
window = tkinter.Tk()
button = tkinter.Button(window, text = 'Hello world' , command=hello)
button.pack()
window.mainloop()
