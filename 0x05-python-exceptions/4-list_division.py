#!/usr/bin/python3
# Divides element by element 2 lists

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(0, list_length):
        try:
            calc = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            calc = 0
        except ZeroDivisionError:
            print("division by 0")
            calc = 0
        except IndexError:
            print("out of range")
            calc = 0
        finally:
            n_list.append(calc)
    return (n_list)
