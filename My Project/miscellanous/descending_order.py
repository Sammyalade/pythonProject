def sort_list_in_descending_order(numbers):
    for count in range(len(numbers)):
        for index in range(len(numbers)):
            if numbers[count] > numbers[index]:
                numbers[count] = numbers[count] + numbers[index]
                numbers[index] = numbers[count] - numbers[index]
                numbers[count] = numbers[count] - numbers[index]
    return f"{numbers}"

print(sort_list_in_descending_order([10, 2, 8, 9, 3, 4, 1, 5]))