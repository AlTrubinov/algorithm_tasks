import copy


def sum_task(n: int, m: int):
    if n > m:
        return "Указанное число n меньше числа m"
    str_nums = [str(elem) for elem in range(1, n+1)]
    list_of_nums = []
    for i in range(0, n+1):
        for k in range(i+1, n+1):
            int_part_of_sum = int(''.join(str_nums[i:k]))
            if int_part_of_sum < m:
                list_of_nums.append(int_part_of_sum)
    list_of_nums.sort()
    for index in range(len(list_of_nums)-1, -1, -1):
        list_of_index = []
        list_of_checked_nums = copy.deepcopy(list_of_nums)
        for checked_num_ind in range(len(list_of_checked_nums)-1, -1, -1):
            for digit in str(list_of_nums[checked_num_ind]):
                if digit in str(list_of_nums[index]):
                    list_of_checked_nums.pop(checked_num_ind)
                    break
        sum_of_elements = list_of_nums[index]
        for sec_index in range(len(list_of_checked_nums)-1, -1, -1):
            flag = True
            if sum_of_elements + list_of_checked_nums[sec_index] < m:
                sum_of_elements += list_of_checked_nums[sec_index]
                list_of_index.append(sec_index)
            elif sum_of_elements + list_of_checked_nums[sec_index] == m:
                sum_of_elements += list_of_checked_nums[sec_index]
                list_of_index.append(sec_index)
                list_of_index.sort()
                list_of_str_parts = [str(list_of_nums[index]),]
                for ind in list_of_index:
                    list_of_str_parts.append(str(list_of_checked_nums[ind]))
                list_of_str_parts.sort()
                return_mess = "+".join(list_of_str_parts)
                for str_num in str_nums:
                    if str_num not in return_mess:
                        flag = False
                        break
                if flag and len(return_mess) < 2*n-1:
                    return f'{return_mess}={m}'
                # else:
                #     sum_of_elements -= list_of_nums[min(list_of_index)]
                #     list_of_index.remove(min(list_of_index))
    return "Неверное число m"




    # return f'{"+".join([number for number in str_nums])}={m}'

print(sum_task(int(input('Введите число n ')), int(input('Введите число m '))))