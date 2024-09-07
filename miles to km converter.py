from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())    # Assign to, and retrieve input.
    km = round(miles * 1.609, 2)        # rounded to 2 decimal places
    km_result.config(text=f"{km}")      # km result (0) becomes new km result.

window = Tk()
window.title("Miles To Km Converter")
window.minsize(width=350, height=200)
window.config(padx=10, pady=10)

# Label
miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.place(x=250, y=50)

km_input = Label(text="Km", font=("Arial", 12, "normal"))
km_input.place(x=250, y=90)

km_result = Label(text=f"0", font=("Arial", 12, "normal"))
km_result.place(x=150, y=90)

is_equal = Label(text="is equal to", font=("Arial", 12, "normal"))
is_equal.place(x=20, y=90)

# #Button
calculate = Button(text="Calculate", command=miles_to_km)   # , command ?
calculate.place(x=150, y=120)

# Entry
miles_input = Entry(width=10)
miles_input.place(x=150, y=55)


window.mainloop()
