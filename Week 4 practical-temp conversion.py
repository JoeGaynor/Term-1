def celsius(f, i):
    if i == 0:
        return (f-32)*(5/9)
    if i == 1:
        return f-273.15


def fahrenheit(c, i):
    if i == 0:
        return c*(9/5)+32
    if i == 1:
        k_to_c = celsius(c, 1)
        return fahrenheit(k_to_c, 0)


def kelvin(c, i):
    if i == 0:
        return c-273.15
    elif i == 1:
        return c+273.15
    elif i == 2:
        return celsius(c, 0) + 273.15


valid_temp = False
while 1:
    while valid_temp is not True:
        temp = input("please enter a temperature: ")
        try:
            if temp[-1].lower() == "c" or temp[-1].lower() == "f" or temp[-1].lower() == "k":
                final_temp = int(temp[:len(temp) - 1])
            else:
                final_temp = int(temp)

            valid_temp = True
        except ValueError:
            print("Please enter an actual number")

    valid_temp = False
    selection = input("What temp conversion do you want?\nc-f, c-k, f-c, f-k, k-c, k-f: ")
    if selection.lower() == "c-f":
        print(f"in fahrenheit, that is: {fahrenheit(final_temp, 0)}")
    elif selection.lower() == "c-k":
        print(f"in kelvin, that is: {kelvin(final_temp, 1)}")
    elif selection.lower() == "f-c":
        print(f"in celsius, that is: {celsius(final_temp, 0)}")
    elif selection.lower() == "f-k":
        print(f"in kelvin, that is: {kelvin(final_temp, 2)}")
    elif selection.lower() == "k-c":
        print(f"in celsius, that is: {celsius(final_temp, 1)}")
    elif selection.lower() == "k-f":
        print(f"in fahrenheit, that is: {fahrenheit(final_temp, 1)}")
    else:
        print("Invalid selection")
        valid_temp = True
