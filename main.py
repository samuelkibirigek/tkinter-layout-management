from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("tkinter layout management")
window.config(padx=20, pady=20)

#Label to be placed in the top left corner
#I opt to use the grid method over place and pack

label = Label(text="This is the label")
label.grid(column=0, row=0)
label.config(padx=30, pady=20)

button = Button(text="Button")
button.grid(column=1, row=1)
button.config(padx=10, pady=30)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
new_button.config(padx=30, pady=20)

the_input = Entry()
the_input.grid(column=3, row=2)
the_input.config(width=20)




window.mainloop()