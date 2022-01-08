import webbrowser
import tkinter
from tkinter import *
from tkinter import Entry


if __name__ == '__main__':

    app = Tk()
    app.geometry("600x400")
    app.title("Upgraded searcher")

    url_label = Label(app, text="Where do you want to search for ? (Twitter, Reddit, Instagram)")
    url_label.pack()

    user_input = Text(app, width = 20, height = 1)
    user_input.pack()

    username_label = Label(app, text="Username")
    username_label.pack()

    text = Text(app, width=20, height=1)
    text.insert(END, "")    
    text.pack()

    def copy():
        username.config(text=""+text.get(1.0, "end-1c"))

    btn_Copy = Button(app, text="Copy", command=copy)
    btn_Copy.pack()

    username = Label(app, text="")
    username.pack()

    def find():
        if user_input.get(1.0, "end-1c") == "Instagram":
            URL_instagram = "https://www.instagram.com/{0}/".format(username.cget("text"))
            webbrowser.open(URL_instagram, new = 1)
        if user_input.get(1.0, "end-1c") == "Reddit":
            URL_reddit = "https://www.reddit.com/user/{0}/".format(username.cget("text"))
            webbrowser.open(URL_reddit,new=1)
        if user_input.get(1.0, "end-1c") == "Twitter":
            URL_twitter = "https://twitter.com/{0}".format(username.cget("text"))
            webbrowser.open(URL_twitter,new=1)

    btn_Find = Button(app, text="Find", command=find)
    btn_Find.pack()
    
    app.mainloop()