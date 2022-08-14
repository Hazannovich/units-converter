from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Distance Units Converter")
window.minsize(width=50, height=50)
window.config(padx=20, pady=20)

# Entries
entry = Entry(width=5)
# Add some text to begin with
entry.insert(index=END, string="")
entry.focus()
# Gets text in entry
entry.grid(column=1, row=0)


def convert_to_miles(event=None):
    radio_state.set(2)
    convert_from_label.config(text="Km")
    convert_to_label.config(text="Miles")
    txt = entry.get()[:-1]
    entry.delete(0, 'end')
    entry.insert(0, txt)


def convert_to_km(event=None):
    radio_state.set(1)
    convert_from_label.config(text="Miles")
    convert_to_label.config(text="Km")
    txt = entry.get()[:-1]
    entry.delete(0, 'end')
    entry.insert(0, txt)


# Radiobutton
radio_state = IntVar()
radiobutton1 = Radiobutton(text="miles to km(A)", value=1, variable=radio_state, command=convert_to_km)
radiobutton2 = Radiobutton(text="km to miles(S)", value=2, variable=radio_state, command=convert_to_miles)
radiobutton1.grid(column=0, row=2)
radiobutton2.grid(column=1, row=2)
radio_state.set(1)
window.bind('a', convert_to_km)
window.bind('s', convert_to_miles)
# Labels
convert_from_label = Label(text="Miles")
convert_from_label.grid(column=2, row=0)

equal_label = Label(text=f"is equal to")
equal_label.grid(column=0, row=1)

convert_to_label = Label(text="Km")
convert_to_label.grid(column=2, row=1)
output_label = Label(text="")
output_label.grid(column=1, row=1)


# Buttons
def calculate(event=None):
    found_error = False
    bad_input = "BAD INPUT!"
    try:
        if radio_state.get() == 1:
            miles_input = float(entry.get())
            in_km = miles_input * 1.609
            output_label.config(text=in_km)
        else:
            km_input = float(entry.get())
            in_miles = km_input * 0.621371192
            output_label.config(text=in_miles)
    except ValueError:
        found_error = True
    finally:
        if found_error:
            output_label.config(text=bad_input)


window.bind('<Return>', calculate)

# calls action() when pressed
button = Button(window, text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
