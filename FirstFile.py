def swap_case(input):
    output = ''
    for i in range(len(input)):
        if input[i].islower():
            output += input[i].upper()

        else:
            output += input[i].lower()

    return output

print(swap_case('Fanis'))
