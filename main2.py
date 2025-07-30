import tkinter
import pyshorteners
root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("500x250")
def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0,short_url)
    
longurl_label = tkinter.Label(root, text = "Enter long url")
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root,text = "Output Shortened URL")
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root,text = "Shorten URL",command = shorten)

#use geometry managers
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()


root.mainloop()
