# 1) https://www.codewars.com/kata/583f158ea20cfcbeb400000a
def arithmetic(a, b, operator):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]


# 2) https://www.codewars.com/kata/529eef7a9194e0cbc1000255
def is_anagram(test, original):
    list1 = []
    for letter in test.lower():
        list1.append(letter)
        
    list2 = []
    for letter in original.lower():
        list2.append(letter)
    
    list1.sort()
    list2.sort()

    return list1 == list2

# 3) https://www.codewars.com/kata/52f3149496de55aded000410
def sum_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total
# 4) https://www.codewars.com/kata/545a4c5a61aa4c6916000755
def gimme(input_array):
    numbers = []
    for num in input_array:
        numbers.append(num)
    numbers.sort()
    middle_number = numbers[1]
    return input_array.index(middle_number)