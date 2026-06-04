# 1)შექმენით ფუნქცია რომელიც დაბეჭდავს თქვენს სახელს და გვარს
def my_name():
    print("goga narimanidze")
my_name()


# 2)უნდა შევქმნათ ფუნქცია , რომელსაც პარამეტრად გადაეცემა რიცხვი , ამ ფუნქციამ უნდა გაიგოს ეს რიცხვი ლუწი იქნება თუ კენტი
def number_type (number):
    if number % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
number_type(3)