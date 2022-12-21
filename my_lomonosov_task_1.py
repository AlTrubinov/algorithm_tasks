def string_separator(string: str, list_of_parts: list, f_p: str = ''):

    for index in range(1, len(string)):
        first_part = f_p + string[:index] + '+'
        second_part = string[index:]
        if len(second_part) == 1:
            list_of_parts.append([f'{first_part}{second_part}'])
        else:
            list_of_parts.append([f'{first_part}{second_part}'])
            string_separator(second_part, list_of_parts, first_part)


def sum_task(n: int, m: int):
    if n > m:
        return "Указанное число n больше числа m"
    str_nums = [str(elem) for elem in range(1, n + 1)]
    list_of_string_parts = []
    string_of_nums = ''.join(str_nums)
    list_of_string_parts.append(string_separator(string_of_nums, list_of_string_parts))
    for combination in list_of_string_parts[:-1]:

        str_term_list = combination[0].split('+')
        int_term_list = [int(term) for term in str_term_list]
        if sum(int_term_list) == m:
            return f'{combination[0]}={m}'
    return "Неверное число m"


print(sum_task(int(input('Введите число n ')), int(input('Введите число m '))))