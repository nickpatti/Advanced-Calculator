from calculator_data import ScientificLists
import math


class ScientificFunctions(ScientificLists):
    def number_press(number):
        if "." in ScientificLists.num and number == ".":
            pass
        else:
            # append the entered number into a list
            ScientificLists.num.append(number)

        # iterate through num list to join together each number with no spaces
            ScientificLists.lower_label_list.append("".join(str(x) for x in ScientificLists.num))

            for x in range(len(ScientificLists.lower_label_list) - 1):
                del ScientificLists.lower_label_list[0]
            # created list temp as the current number on the screen
            print(ScientificLists.lower_label_list)
            ScientificLists.temp.append(ScientificLists.lower_label_list[-1])
        # need to return the last entry in lower_label_list to set the lower screen, problem with this is that the list could get very long
        return ScientificLists.lower_label_list[-1]

    # operation to get operators and add them to a label

    def operator_press(operation):
        ScientificLists.operator.append(operation)

        # use this for loop to iterate over each number and append it to the equation list, also add the operator
        # temp is used if equals has been pressed -  this is to keep the previous answer so the equation can be built upon
        if len(ScientificLists.temp) > 1:
            ScientificLists.equation.append(ScientificLists.operator[-1])
            ScientificLists.equation.insert(0, '(')
            ScientificLists.equation.insert(-1, ')')
            # clear temp so next operator is in the correct place and brackets aren't added willy nilly
            ScientificLists.temp.clear()
        else:
            ScientificLists.equation.append(ScientificLists.lower_label_list[0])
            for i in ScientificLists.operator:
                ScientificLists.equation.append(i)

        ScientificLists.upper_label_list.append(" ".join(str(x) for x in ScientificLists.equation))
        ScientificLists.lower_label_list.clear()
        # remove number from buttom row, then clear the bottom label
        ScientificLists.num.clear()
        ScientificLists.operator.clear()
        # clear the lower label ready for the next entry
        return ScientificLists.upper_label_list[-1]

    def equals_press(e):
        ScientificLists.equation.append(ScientificLists.lower_label_list[0])
        print(ScientificLists.equation)
        ScientificLists.upper_label_list.append("".join(str(x) for x in ScientificLists.equation))
        ScientificLists.num.clear()
        ScientificLists.operator.clear()
        output = eval("".join(str(x) for x in ScientificLists.equation))
        ScientificLists.lower_label_list.append(output)
        for x in range(len(ScientificLists.lower_label_list) - 1):
            del ScientificLists.lower_label_list[0]
        # ScientificLists.equation.clear()
        ScientificLists.temp.append(output)
        return ScientificLists.upper_label_list[-1], ScientificLists.lower_label_list[-1]

    def clear_all():
        ScientificLists.num.clear()
        ScientificLists.equation.clear()
        ScientificLists.lower_label_list.clear()
        ScientificLists.upper_label_list.clear()
        ScientificLists.temp.clear()
        return ScientificLists.lower_label_list, ScientificLists.upper_label_list

    def clear_entry():
        ScientificLists.num.clear()
        ScientificLists.lower_label_list.clear()
        return ScientificLists.lower_label_list

    def percent(n):
        ScientificLists.upper_label_list.clear()
        convert = float(ScientificLists.lower_label_list[0]) / 100
        ScientificLists.equation.append(convert)
        print(ScientificLists.equation)
        ScientificLists.upper_label_list.append("".join(str(x) for x in ScientificLists.equation))

        output = eval("".join(str(x) for x in ScientificLists.equation))
        ScientificLists.lower_label_list.append(output)
        for x in range(len(ScientificLists.lower_label_list) - 1):
            del ScientificLists.lower_label_list[0]
        # ScientificLists.equation.clear()
        ScientificLists.temp.append(output)

        return ScientificLists.lower_label_list[-1], ScientificLists.upper_label_list[-1]

    def square_root():
        # add to both num and equation lists
        output = (math.sqrt(float(ScientificLists.lower_label_list[-1])))
        ScientificLists.lower_label_list.append(output)
        # make sure only display is in the lower label list
        for x in range(len(ScientificLists.lower_label_list) - 1):
            del ScientificLists.lower_label_list[0]

        ScientificLists.equation.append(ScientificLists.lower_label_list[0])
        ScientificLists.temp.append(ScientificLists.lower_label_list[0])

        return ScientificLists.lower_label_list[-1]

    def factorial(n):
        s = [str(i) for i in n]
        factor = int("".join(s))
        # create how the factorial should be notated in the upper label
        upper_label.append("".join(str(x) for x in ScientificLists.num) + '!')
        output = 1
        if factor >= 1:
            for i in range(1, factor + 1):
                output = output * i

        # keep the output so that more functions can be applied to the number
        ScientificLists.num.clear()
        ScientificLists.num.append(output)
        lower_label.append(output)

    def log(n):
        input_number = int(n.get())
        output = (math.log(float(input_number)))
        ScientificLists.lower_label_list.append(output)
        ScientificLists.equation.append(output)
        ScientificLists.temp.append(ScientificLists.lower_label_list[0])
        return output

    def tax(n):
        input_number = int(n.get())
        if input_number <= 12500:
            output = input_number
        elif input_number > 12500 and input_number < 30000:
            tax = (input_number - 12500) * 0.2
            output = input_number - tax
        elif input_number > 30000:
            part1 = (input_number - 30000) * 0.6
            part2 = (input_number - 42500) * 0.8
            output = part1 + part2
        return output


12500
