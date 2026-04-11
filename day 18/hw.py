# # 1) 200 დან 500 მდე დაპრინტეთ 4-ის და 7-ის საერთო ჯერადები (ეს დავალება გააკეთეთ ორ ვარიანტში -> for ციკლითაც და while ციკლლითაც)
# for i in range(200 , 500):
#     if i % 4 == 0 and i % 7 == 0:
#         print(i)

# # 2) 300 დან 1000 მდე დაპრინტეთ 3-ის ან 10-ის ჯერადები (ეს დავალება გააკეთეთ ორ ვარიანტში -> for ციკლითაც და while ციკლლითაც)
# for i in range (300, 1000):
#     if i % 3 == 0 or i % 10 == 0:
#         print (i)
# number = 300
# while number < 1000:
#     if number % 3 == 0 or number % 10 == 0:
#         print (number)
#     number = number + 1

# # 3) 1 დან 50 მდე დაპრინტეთ ყველა რიცხვი:
# #  - ლუწი რიცხვებისთვის დაწერეთ "Even: (რიცხვი)"
# #  - კენტი რიცხვებისთვის დაწერეთ "Odd: (რიცხვი)"
# for i in range(1,50):
#     if i % 2 == 0:
#         print ("even:" + str(i))
#     else:
#         print("odd:"+ str(i))

# # 4) მომხმარებელს შემოატანინეთ 10 რიცხვი და:
# #  - დათვალეთ რამდენი არის დადებითი
# #  - რამდენი არის უარყოფითი
# #  - ბოლოს დაპრინტეთ შედეგები
# pos = 0
# neg = 0
# for i in range(10):
#     num = int(input("enter a number: "))
#     if num > 0:
#         pos = pos + 1
#     else:
#         neg = neg + 1
# print ("positive numbers:" + str(pos))
# print ("negative numbers:" + str(neg))


# # 5) მომხმარებელს შემოატანინეთ რიცხვი და:
# #  - თუ რიცხვი იყოფა 2-ზე და 3-ზე -> დაპრინტეთ "Good"
# #  - თუ მხოლოდ 2-ზე იყოფა -> "Two"
# #  - თუ მხოლოდ 3-ზე იყოფა -> "Three"
# #  - სხვა შემთხვევაში -> "None"
# number = int(input("enter a number"))
# if number % 2 == 0 and number % 3 == 0:
#     print("good")
# elif number % 2 == 0 and number % 3 != 0:
#     print("two")
# elif number % 2 != 0 and number % 3 == 0:
#     print ("three")
# else:
#     print ("none")

# # 6) 1 დან 100 მდე დაპრინტეთ ყველა რიცხვი, მაგრამ:
# # - თუ რიცხვი იყოფა 3-ზე -> დაპრინტეთ "Fizz"
# # - თუ იყოფა 5-ზე -> დაპრინტეთ "Buzz"
# # - თუ ორივეზე იყოფა -> დაპრინტეთ "FizzBuzz"
# # - სხვა შემთხვევაში -> თავად რიცხვი
# for i in range(1,100):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print ("fizzbuzz")
#     else:
#         print (i)

# # 7) შექმენით პროგრამა, რომელიც მომხმარებელს რიცხვს შემოატანინებს მანამ სანამ 0-ს არ შეიყვანს:
# #  - დადებითი რიცხვების რაოდენობა დაითვალეთ
# #  - უარყოფითებისაც
# #  - ბოლოს(ანუ როცა 0 შემოიყვანა) დაპრინტეთ ეს რაოდენობები

# negative= 0
# positive = 0
# number = int(input("enter a number"))
# while number != 0:
#     if number > 0:
#         positive = positive + 1
#         number = int(input("enter a number (0 to stop)"))
#     elif number < 0:
#         negative = negative + 1
#         number = int(input("enter a number (0 to stop)"))
# print ("number of positives are: " + str(positive))
# print( "number of negatives are: " + str(negative))

# 8) მომხმარებელს შემოატანინეთ რიცხვი და:
# - დაპრინტეთ 1 დან ამ რიცხვამდე ყველა რიცხვი
# - მაგრამ გამოტოვეთ ის რიცხვები, რომლებიც იყოფა 4-ზე
number = int(input("enter a number:"))
for i in range(1, number):
    if i % 4 != 0:
        print(i)






