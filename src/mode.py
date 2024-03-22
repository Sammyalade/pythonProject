def check_for_mode(*numbers_list):
    my_mode = max(set(numbers_list), key=numbers_list.count)
    my_mode_count = numbers_list.count(my_mode)
    return my_mode, my_mode_count


numbers = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
mode, mode_count = check_for_mode(*numbers)
print(f"[{mode_count},{mode}]")

