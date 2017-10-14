def swap_case(input):
    output = ''
    for i in range(len(input)):
        if input[i].islower():
            output += input[i].upper()

        else:
            output += input[i].lower()

    return output


list = []
list.append(1)
list.append(2)
list.append(3)
print(list.pop(0))
print (list)
