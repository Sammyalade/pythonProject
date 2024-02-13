def swap(string_1, string_2):
    temp = ''
    temp2 = ''
    for number in range(len(string_1)):
        if number == len(string_1) - 1:
            temp += string_2[len(string_2) - 1]
            continue
        temp += string_1[number]
    for number in range(len(string_2)):
        if number == len(string_2) - 1:
            temp2 += string_1[len(string_1) - 1]
            continue
        temp2 += string_2[number]

    return temp2 + " " + temp


def swap_second_try(string_1, string_2):
    return string_2[:-1] + string_1[len(string_1) - 1::1] + ' ' + string_1[:-1] + string_2[len(string_2) - 1::1]


print(swap_second_try("abc", "xyz"))
