from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")


# function to convert miles to km
def convert():
    miles = float(miles_input.get())
    km_value = miles * 1.609
    output_km_label.configure(text=f"{km_value}")


# Textbox to enter the miles that needs to be converted
miles_input = Entry()
miles_input.grid(column=1, row=0)
window.config(padx=20, pady=20)

# label to represent miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# label to represent is equal to
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# output field to show converted miles to km
output_km_label = Label(text="0")
output_km_label.grid(column=1, row=1)

# label to represent km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button to convert miles to km
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
