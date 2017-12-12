from hanc_combined_codes import*
from tkinter import*

def click():
    key1 = int(entry_1.get()) #this will collect the text from the entry box
    crypt1 = entry_2.get()
    use_mgs1 = entry3.get()
    transl_text = HancSecurity(key1, use_mgs1, crypt1)
    try1 = transl_text.crypting()
    output2.delete(0.0, END)
    try:
        mycipher = try1
    except:
        mycipher = "Sorry, something is wrong with your input. Please check again."
    output2.insert(END, mycipher)
def close_window():
    wn.destroy()
    exit()

wn = Tk()
wn.title("HancSecurity")
wn.configure(background = "lightgreen")

label1 = Label(wn, text="Have fun texting your friend securely!", bg = "red", fg = "black", font = "none 12 bold")
label1.grid(row = 1, column = 0, sticky = W)

label2 = Label(wn, text ="Your Key < 100", bg = "blue", fg = "yellow", font = "none 12 bold")
label2.grid(row = 2, column = 0, sticky = W)
label3 = Label(wn, text ="encrypt or decrypt", bg = "blue", fg = "yellow", font = "none 12 bold")
label3.grid(row = 2, column = 1, sticky = W)

entry_1 = Entry(wn, width = 20, bg = "white")
entry_1.grid(row = 3, column = 0, sticky = W)
entry_2 = Entry(wn, width = 24, bg = "white")
entry_2.grid(row = 3, column = 1, sticky = W)
bt1 = Button(wn, text= "Crypting", width = 8, command = click)
bt1.grid(row = 3, column = 2, sticky = W)

entry3 = Entry(wn, width = 100, bg = "white")
entry3.grid(row=5, column = 0, columnspan=3, sticky=W)

label4 = Label(wn, text ="Below is your translation. Feel free to try to find the algorithm. Thank you", bg = "blue", fg = "yellow", font = "none 12 bold")
label4.grid(row = 6, column = 0, sticky = W)
output2 = Text(wn, width = 100, height = 10, wrap = WORD, background = "white")
output2.grid(row=7, column = 0, columnspan=3, sticky=W)


label5 = Label(wn, text="Click to exit:", bg = "black", fg = "white", font = "none 12 bold")
label5.grid(row = 8, column = 0, sticky = S)
Button(wn, text = "Exit", width = 13, command = close_window).grid(row=9, column = 0, sticky = S)


wn.mainloop()

