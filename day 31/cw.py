# 1) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ იწყება თუ არა ეს წინადადება ამ სიტყვით
text = input("enter random words: ")
word = input("enter one word: ")
print(text.startswith(word))

# 2) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ მთავრდება თუ არა ეს წინადადება ამ სიტყვით
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
if sentence.endswith(word):
    print("the sentence ends with this word.")
else:
    print("the sentence does not end with this word.")
# 3) მომხმარებელს მოთხოვეთ რაიმე ჩამოთვალოს თავისი საყვარელი ფერები(input ით).
#  გამოიყენეთ split მეთოდი და დაპრინტეთ მიღებული სია 
fav_colours = input("enter your favorite colors: ")
fav_colours = fav_colours.split()
print(fav_colours)

# 4) მომხმარებელს მოთხოვეთ შემოიყვანოს რიცხვები(input ით).
#  გადაქციეთ ეს სტრინგი სიად ოღონდ ისე, რომ საბოლოო სია შეიცავდეს ინტეჯერებს 

numbers = input("enter some numbers: ")
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)

