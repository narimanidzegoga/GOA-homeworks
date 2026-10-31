# 1) https://www.codewars.com/kata/5ab6538b379d20ad880000abS
def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)
# 2) https://www.codewars.com/kata/55cbc3586671f6aa070000fb
def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False
# 3) https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    if arr == None:
        return 0

    if len(arr) <= 1:
        return 0

    arr.remove(min(arr))
    arr.remove(max(arr))

    total = 0

    for i in arr:
        total = total + i

    return total


# 4) https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
        
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    else:
        return "Error"


# 5) https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
        
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives = count_positives + 1
        elif num < 0:
            sum_negatives = sum_negatives + num
            
    return [count_positives, sum_negatives]



