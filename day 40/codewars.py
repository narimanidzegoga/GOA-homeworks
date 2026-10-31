# 1) https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total = total + num
    return total

# 2) https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
def repeat_str(repeat, string):
    return string * repeat

# 3) https://www.codewars.com/kata/57f781872e3d8ca2a000007e
def remove_char(s):
    return s[1:-1]

# 4) https://www.codewars.com/kata/515e271a311df0350d00000f
def square_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i] * numbers[i]
    return total

# 5) https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

# 6) https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total = total + i
    return total

# 7) https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    total = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            total = total + 1
    return total







