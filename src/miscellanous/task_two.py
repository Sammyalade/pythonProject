def collect_ten_input_without_saving_duplicate(input_list) -> list:
    list1 = []
    for item in input_list:
        if item not in list1:
            list1.append(item)

    return list1


print(collect_ten_input_without_saving_duplicate([1, 4, 2, 5, 6, 2, 3, 3, 1, 6, 9, 7]))


def sum_collection(set1) -> int:
    total = 0
    for item in set1:
        total += item

    return total


print(sum_collection({1, 3, 4, 6, 8, 9}))


def remove_item(set1, item):
    set2 = set()
    for item1 in set1:
        if item1 == item:
            continue
        else:
            set2.add(item1)
    if set1 == set2:
        return None
    return set2


print(remove_item({1, 3, 4, 6, 8, 9}, 9))
print(remove_item({1, 3, 4, 6, 8, 9}, 15))


def find_intersection(set1, set2):
    set_for_intersect = set()
    for item in set1:
        if item in set2:
            set_for_intersect.add(item)

    if len(set_for_intersect) > 0:
        return set_for_intersect
    return None


print(find_intersection({1, 3, 4, 6, 8, 9}, {1, 10, 16, 4, 6, 30}))
print(find_intersection({1, 3, 4, 6, 8, 9}, {10, 16, 30}))
