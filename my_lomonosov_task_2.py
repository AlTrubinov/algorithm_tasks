list_1 = [-3, 2, 3, 4, 5, 6, 7, 7, 8]
list_2 = [-1, -1, -1, -1]
list_3 = [1, 2, 3, 4, 5, 6]
list_4 = [1, 1, 2, 3, 4, 4]
list_5 = [1, 2, -3, 1, 2, 3, 2]
list_6 = [-1, -1, -1, -1, 1]
list_7 = [6, 7, 6, 5, 4, 3, 2, 1]


def border_search(searched_list):
    set_list = set(searched_list)
    if len(set_list) == len(searched_list) or len(set_list) == 1:
        return f'{0}, {len(set_list) - 1}'

    first_pointer, second_pointer = 0, 0
    list_of_borders = []
    max_range = 0
    index_max_borders = 0

    while second_pointer < len(searched_list) - 1:
        if searched_list[second_pointer] < searched_list[second_pointer + 1]:
            second_pointer += 1
        else:
            list_of_borders.append([first_pointer, second_pointer])
            second_pointer += 1
            first_pointer = second_pointer

    list_of_borders.append([first_pointer, second_pointer])

    first_pointer, second_pointer = 0, 0

    while second_pointer < len(searched_list) - 1:
        if searched_list[second_pointer] > searched_list[second_pointer + 1]:
            second_pointer += 1
        else:
            list_of_borders.append([first_pointer, second_pointer])
            second_pointer += 1
            first_pointer = second_pointer

    list_of_borders.append([first_pointer, second_pointer])

    for index in range(len(list_of_borders)):
        left_border = list_of_borders[index][0]
        right_border = list_of_borders[index][1]
        difference = abs(right_border - left_border)
        if difference > max_range:
            max_range = difference
            index_max_borders = index
    return f'{list_of_borders[index_max_borders][0]}, {list_of_borders[index_max_borders][1]}'


print(border_search(list_7))
