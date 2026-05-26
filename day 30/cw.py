# 1) მომხმარებელს მოთხოვეთ რაიმე წინადადება/სიტყვა.
#   - დაითვალეთ რამდენი დიდი და რამდენი პატარა ასო არის ამ სტრინგში
#   - დაპრინტეთ შედეგები

small = 0
big = 0

random_text = input("enter random words: ")

for i in range(len(random_text)):
    if random_text[i] == random_text[i].upper():
        big = big + 1
    elif random_text[i] == random_text[i].lower():
        small = small + 1

print(big)
print(small)

