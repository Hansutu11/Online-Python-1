my_string_list = ["Hans ", "Ashely ", "Braden"]
my_num_list = [2, 32, 31, 11, 22]
my_mixed_list = ["Seattle ", 44, "Money ", 66, "Seahawks ", 130,]


def identify_list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(my_mixed_list)
print identify_list_type(my_num_list)
print identify_list_type(my_string_list)
