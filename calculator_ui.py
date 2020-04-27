import tkinter as tk
from tkinter.ttk import *
from calculator_functions import ScientificFunctions
from calculator_data import ScientificLists


class Calculator():

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        # create and place screen elements -  let upper half reflect previous sum, lower half should show most recent number or operation
        upper_label = tk.StringVar()
        lower_label = tk.StringVar()

        labels = (upper_label, lower_label)

        def set_label(n):
            ScientificFunctions.operator_press(n)
            upper_label.set(ScientificLists.upper_label_list[-1])
            lower_label.set("")

        def set_equals(e):
            ScientificFunctions.equals_press(e)
            upper_label.set(ScientificLists.upper_label_list[-1])
            lower_label.set(ScientificLists.lower_label_list[-1])

        def set_clear_all():
            ScientificFunctions.clear_all()
            upper_label.set("")
            lower_label.set("")

        def set_percent(n):
            ScientificFunctions.percent(n)
            lower_label.set(ScientificLists.lower_label_list)
            upper_label.set(ScientificLists.upper_label_list)

        def set_square_root():
            ScientificFunctions.square_root()
            lower_label.set(ScientificLists.lower_label_list[-1])

        # this will help me out later, will append each number and operator to the following lists

        screen_upper = Label(frame, textvariable=upper_label)
        screen_lower = Label(frame, textvariable=lower_label)

        clear_all = Button(frame, text="C", command=lambda: set_clear_all())
        clear_entry = Button(frame, text="CE", command=lambda n="": lower_label.set(ScientificFunctions.clear_entry()))
        percentage = Button(frame, text="%", command=lambda n='%': set_percent(n))
        squared = Button(frame, text="x^2", command=lambda n="**2": set_label(n))
        power = Button(frame, text="x^y", command=lambda n="**": lower_label.set(ScientificFunctions.number_press(n)))
        open_bracket = Button(frame, text="(", command=lambda n="(": set_label(n))
        close_bracket = Button(frame, text=")", command=lambda n=")": set_label(n))
        factorial_button = Button(frame, text="n!", command=lambda n='': ScientificFunctions.factorial(n))
        square_root_button = Button(frame, text="sqrt", command=lambda: set_square_root())
        log_button = Button(frame, text="log()", command=lambda n=lower_label: lower_label.set(ScientificFunctions.log(n)))
        tax = Button(frame, text="tax", command=lambda n=lower_label: lower_label.set(ScientificFunctions.tax(n)))

        screen_upper.grid(row=0, column=0, columnspan=6)
        screen_lower.grid(row=1, column=0, columnspan=6)
        percentage.grid(row=3, column=2)
        clear_entry.grid(row=3, column=3)
        clear_all.grid(row=3, column=4)
        squared.grid(row=4, column=0)
        power.grid(row=5, column=0)
        open_bracket.grid(row=4, column=1)
        close_bracket.grid(row=4, column=2)
        factorial_button.grid(row=4, column=3)
        square_root_button.grid(row=6, column=0)
        log_button.grid(row=7, column=0)
        tax.grid(row=8, column=0)

        # NUMBER PAD
        # create buttons 1-9, need to be reversed, need to create a button dict
        number_pad = {}
        num_pad_row = 5
        num_pad_col = 3

        for x in reversed(range(1, 10)):
            # use -1 to ensure 1, 4 and 7 are the leftmost numbers
            number_pad[x] = Button(frame, text=x, command=lambda n=x: lower_label.set(ScientificFunctions.number_press(n)))
            number_pad[x].grid(row=num_pad_row, column=num_pad_col)
            num_pad_col -= 1

            # need to reset the positioning so there are three numbers on each row
            if num_pad_col < 1:
                num_pad_col = 3
                num_pad_row += 1

        # insert operator buttons
        operator_symbols = ["/", "*", "-", "+"]
        operator_buttons = {}
        num_pad_col = 4
        num_pad_row = 4

        for x in operator_symbols:
            operator_buttons = Button(frame, text=x, command=lambda n=x: set_label(n))
            operator_buttons.grid(row=num_pad_row, column=num_pad_col)
            num_pad_row += 1

            # create 0 and neighbouring buttons and =
        switch_pos_neg = Button(frame, text="+/-", command=lambda n="+/-": ScientificFunctions.operator_press(n))
        zero = Button(frame, text="0", command=lambda n=0: lower_label.set(ScientificFunctions.number_press(n)))
        decimal = Button(frame, text=".", command=lambda n=".": ScientificFunctions.number_press(n))
        equals = Button(frame, text="=", command=lambda n="=": set_equals(n))

        switch_pos_neg.grid(row=8, column=1)
        zero.grid(row=8, column=2)
        decimal.grid(row=8, column=3)
        equals.grid(row=8, column=4)


root = tk.Tk()
view = Calculator(root)
root.mainloop()
