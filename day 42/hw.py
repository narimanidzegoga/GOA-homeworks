# 1) ახსენით რა არის `tuple` და რით განსხვავდება ის `list`-ისგან.
# tuple არის immutable (მუდმივი) მონაცემთა სტრუქტურა, რომელიც ინახავს ელემენტებს თანმიმდევრობით.
# list კი არის - mutable და მასში ელემენტების დამატება, წაშლა და შეცვლა შესაძლებელია.
# tuple-ი გამოიყენება მაშინ, როცა მნიშვნელობები არ უნდა შეიცვალოს, ხოლო list-ი როცა საჭიროებს შეცვლას.


# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით `tuple`-ს `list`-ის ნაცვლად.
# tuple-ი კარგია გამოსაშვები მონაცემებისთვის, მაგალითად გეოგრაფიული კორდინატები ან კონფიგურაციის პარამეტრები, რომლებიც არ უნდა შეცვალოთ.
# list-ი კი გამოსადეგია მაშინ, როცა მონაცემები უნდა იცვლებოდეს და ელემენტები დაიმატოს ან წაიშალოს.


# 3) შექმენით ფუნქცია first_and_last(items), რომელიც მიიღებს `tuple`-ს და დააბრუნებს ახალ `tuple`-ს, რომელიც შეიცავს მხოლოდ პირველ და ბოლო ელემენტს.
def first_and_last(items):
    return (items[0], items[-1])


# 4) შექმენით ფუნქცია middle_element(items), რომელიც მიიღებს კენტსიგრძიან tuple-ს და დააბრუნებს მის შუა ელემენტს.
def middle_element(items):
    return items[len(items) // 2]


# 5) შექმენით ფუნქცია count_occurrences(items, value), რომელიც მიიღებს tuple-ს და ნებისმიერ მნიშვნელობას, შემდეგ კი დააბრუნებს რამდენჯერ გვხვდება ეს მნიშვნელობა tuple-ში. არ გამოიყენოთ count() მეთოდი.
def count_occurrences(items, value):
    count = 0
    for item in items:
        if item == value:
            count += 1
    return count


# 6) შექმენით ფუნქცია contains_duplicates(items), რომელიც მიიღებს tuple-ს და დააბრუნებს True, თუ მასში რომელიმე ელემენტი მეორდება, წინააღმდეგ შემთხვევაში კი False.
def contains_duplicates(items):
    seen = []
    for item in items:
        if item in seen:
            return True
        seen.append(item)
    return False


# 7) შექმენით ფუნქცია swap_edges(items), რომელიც მიიღებს მინიმუმ ორი ელემენტისგან შემდგარ tuple-ს და დააბრუნებს ახალ tuple-ს, სადაც პირველი და ბოლოს ელემენტები ადგილებს გაცვლიან.
def swap_edges(items):
    if len(items) < 2:
        return items
    items_list = list(items)
    temp = items_list[0]
    items_list[0] = items_list[-1]
    items_list[-1] = temp
    return tuple(items_list)


# 8) მოიძიეთ ინფორმაცია index() მეთოდზე და შექმენით ფუნქცია first_position(items, value), რომელიც დააბრუნებს გადაცემული მნიშვნელობის პირველ ინდექსს.
def first_position(items, value):
    for index, item in enumerate(items):
        if item == value:
            return index
    return -1


# 9) შექმენით ფუნქცია tuple_summary(numbers), რომელიც მიიღებს რიცხვების tuple-ს და დააბრუნებს შემდეგი ფორმატის ტექსტს:
# "რაოდენობა: X | ჯამი: Y | პირველი: A | ბოლო: B"
def tuple_summary(numbers):
    return "რაოდენობა: " + str(len(numbers)) + "  ჯამი: " + str(sum(numbers)) + "  პირველი: " + str(numbers[0]) + "  ბოლო: " + str(numbers[-1])


# 10) შექმენით ფუნქცია reverse_tuple(items), რომელიც მიიღებს tuple-ს და დააბრუნებს მის შებრუნებულ ვერსიას. გამოიყენეთ slicing

def reverse_tuple(items):
    reversed_items = ()
    for item in items:
        reversed_items = (item,) + reversed_items
    return reversed_items




