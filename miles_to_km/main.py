from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(pady=30,padx=60)

miles = Label(text="Miles", font=("Arial", 13))
miles.grid(row=0, column=2)
miles.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to", font=("Arial", 13))
is_equal_to.grid(row=1, column=0)

km = Label(text="Km", font=("Arial", 13))
km.grid(row=1, column=2)

value_of_miles = 0
value_of_km = 0

zmienna = Label(text=value_of_km, font=("Arial", 13))
zmienna.grid(row=1, column=1)

def calculate():
    miles = float(entry.get())
    value_of_km = round(miles*1.609344, 2)
    zmienna.config(text=value_of_km)

button = Button(text = "Calculate", command = calculate)
button.grid(row=2, column=1)


entry = Entry()
entry.insert(END, value_of_miles)
entry.grid(row=0, column=1)


window.mainloop()