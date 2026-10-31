# 1) https://www.codewars.com/kata/5545f109004975ea66000086
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0
# 2) https://www.codewars.com/kata/5966e33c4e686b508700002d
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"

    return str(int(a) + int(b))
# 3) https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
#  - არ გამოიყენოთ .reverse() ან reversed()
def reverse_list(l):
    result = []
    for i in range(len(l)):
        result.insert(0, l[i])
    return result
# 4) https://www.codewars.com/kata/558fc85d8fd1938afb000014
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
# 5) https://www.codewars.com/kata/554e4a2f232cdd87d9000038
def DNA_strand(dna):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for i in range(len(dna)):
        result += pairs[dna[i]]
    return result

# 6) https://www.codewars.com/kata/56269eb78ad2e4ced1000013
def find_next_square(sq):
    root = 1
    
    while root * root < sq:
        root += 1
        
    if root * root == sq:
        return (root + 1) * (root + 1)
    
    return -1

# 7) https://www.codewars.com/kata/544aed4c4a30184e960010f4

def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)
            
    if len(result) == 0:
        return str(integer) + " is prime"
        
    return result


