# 1) შექმენით სია სადაც შეინახავთ რაიმე რიცხვებს, მთელებიც და არამთელებიც.
#   - თქცენი დავალებაა შექმნათ ფუნქცია, რომელიც მიიღებს არგუმენტად სიას.
#   - თქვენმა ფუნქციამ უნდა დაპრინტოს მინიმალური და მაქსიმალური რიცხვები (გამოიყენეთ f string)
#   - და უნდა დააბრუნოს ამ რიცხვების კამი
numbers = [1.1 , 3.14 , 6.7 , 10 , 25]
def min_and_max(numbers):
    smallest_number = min(numbers)
    biggest_number = max(numbers)
    print(f"smallest_number is: {smallest_number}")
    print(f"biggest number iss: {biggest_number}")
    
    return biggest_number + smallest_number
result = min_and_max(numbers)
print(result)

