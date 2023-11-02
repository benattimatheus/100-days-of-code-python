from tkinter import *


def converter():
    miles = miles_input.get()
    converted_value = round(float(miles) * 1.6, 2)
    kilometer_label.config(text=f"{converted_value}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=350, height=100)
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

kilometer_label = Label(text="0")
kilometer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=2)

window.mainloop()
