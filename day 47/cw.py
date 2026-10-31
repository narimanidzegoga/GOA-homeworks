# 1) https://www.codewars.com/kata/55ad04714f0b468e8200001c
from unittest import result


def get_char(c):
    return chr(c)
# 2) https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
def multi_table(number):
    result = ""
    for i in range(1, 11):
        if i < 10:
            result += f"{i} * {number} = {i * number}\n"
        else:
            result += f"{i} * {number} = {i * number}"
    return result
# 3) https://www.codewars.com/kata/5899642f6e1b25935d000161
def merge_arrays(arr1, arr2):

    elements = list(set(arr1 + arr2))
    
    elements.sort()
    
    return elements
# 4) https://www.codewars.com/kata/5951d30ce99cf2467e000013
def pythagorean_triple(integers):
    integers.sort()
    
    a = integers[0]
    b = integers[1]
    c = integers[2]
    
    if (a * a) + (b * b) == (c * c):
        return True
    else:
        return False

# 5) https://www.codewars.com/kata/57f609022f4d534f05000024
def stray(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]

# 6) https://www.codewars.com/kata/5d5ee4c35162d9001af7d699
def sum_of_minimums(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + min(numbers[i])
    return total

# 7) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    strings = []
    for i in range(len(l)):
        if type(l[i]) == int:
            strings.append(l[i])
    return strings
