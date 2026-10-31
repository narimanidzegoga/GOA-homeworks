# 1) ახსენით რა განსხვავებაა union, intersection, difference და symmetric_difference მეთოდებს შორის.
# union - ორივე სეტის გაერთიანება და ერთი სეტში ყველა უნიკალური ელემენტის დაბრუნება.
# intersection - ორივე სეტის საერთო ელემენტების დაბრუნება.
# difference - პირველი სეტის ელემენტები, რომლებიც არ არსებობს მეორე სეტში.
# symmetric_difference - ორივე სეტის უნიკალური ელემენტების დაბრუნება, რომლებიც არ არის საერთო.
# 2) შექმენით ფუნქცია merge_students, რომელიც მიიღებს მოსწავლეების სახელების ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე ჯგუფის ყველა მოსწავლეს.
def merge_students(students1, students2):
    return students1.union(students2)
# 3) შექმენით ფუნქცია common_courses, რომელიც მიიღებს ორი მოსწავლის კურსების set-ებს და დააბრუნებს მხოლოდ იმ კურსებს, რომლებსაც ორივე მოსწავლე სწავლობს.
def common_courses(courses1, courses2):
    return courses1.intersection(courses2)
# 4) შექმენით ფუნქცია only_first, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტებს, რომლებიც მხოლოდ პირველ set-შია.
def only_first(set1, set2):
    return set1.difference(set2)
# 5) შექმენით ფუნქცია different_hobbies, რომელიც მიიღებს ორი ადამიანის ჰობების set-ებს და დააბრუნებს იმ ჰობებს, რომლებიც მხოლოდ ერთ-ერთ ადამიანს აქვს.
def different_hobbies(hobbies1, hobbies2):
    return hobbies1.symmetric_difference(hobbies2)
# 6) შექმენით ფუნქცია all_colors, რომელიც მიიღებს თბილი და ცივი ფერების ორ set-ს და დააბრუნებს ყველა უნიკალურ ფერს.
def all_colors(colors1, colors2):
    return colors1.union(colors2)
# 7) შექმენით ფუნქცია shared_friends, რომელიც მიიღებს ორი მომხმარებლის მეგობრების set-ებს და დააბრუნებს მათ საერთო მეგობრებს.
def shared_friends(friends1, friends2):
    return friends1.intersection(friends2)
# 8) შექმენით ფუნქცია absent_students, რომელიც მიიღებს ყველა მოსწავლისა და გაკვეთილზე მყოფი მოსწავლეების set-ებს და დააბრუნებს გაცდენილი მოსწავლეების set-ს.
def absent_students(all_students, present_students):
    return all_students.difference(present_students)
# 9) შექმენით ფუნქცია unique_products, რომელიც მიიღებს ორი მაღაზიის პროდუქტების set-ებს და დააბრუნებს იმ პროდუქტებს, რომლებიც მხოლოდ ერთ-ერთ მაღაზიაში იყიდება.
def unique_products(products1, products2):
    return products1.symmetric_difference(products2)
# 10) შექმენით ფუნქცია combine_three_sets, რომელიც მიიღებს სამ set-ს და დააბრუნებს მათში არსებულ ყველა უნიკალურ ელემენტს.
def combine_three_sets(set1, set2, set3):
    return set1.union(set2).union(set3)
# 11) შექმენით ფუნქცია common_in_three, რომელიც მიიღებს სამ set-ს და დააბრუნებს მხოლოდ იმ ელემენტებს, რომლებიც სამივე set-ში გვხვდება.
def common_in_three(set1, set2, set3):
    return set1.intersection(set2).intersection(set3)
# 12) შექმენით ფუნქცია first_only_words, რომელიც მიიღებს ორ ტექსტს, თითოეულს გადააქცევს სიტყვების set-ად და დააბრუნებს იმ სიტყვებს, რომლებიც მხოლოდ პირველ ტექსტში გვხვდება.

# 13) შექმენით ფუნქცია different_letters, რომელიც მიიღებს ორ ტექსტს და დააბრუნებს იმ უნიკალურ სიმბოლოებს, რომლებიც მხოლოდ ერთ-ერთ ტექსტში გვხვდება.

# 14) შექმენით ფუნქცია has_common_element, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ ერთი საერთო ელემენტი მაინც აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.

# 15) შექმენით ფუნქცია are_disjoint, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ არცერთი საერთო ელემენტი არ აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.

# 16) შექმენით ფუნქცია exclusive_count, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტების რაოდენობას, რომლებიც მხოლოდ ერთ-ერთ set-ში გვხვდება.

# 17) შექმენით ფუნქცია missing_permissions, რომელიც მიიღებს საჭირო უფლებებისა და მომხმარებლის უფლებების set-ებს და დააბრუნებს იმ უფლებებს, რომლებიც მომხმარებელს აკლია.

# 18) შექმენით ფუნქცია common_numbers, რომელიც მიიღებს ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე set-ში არსებულ რიცხვებს.
#     - არ გამოიყენოთ სეტის მეთოდები!!! no intersection.
#     - გამოიყენეთ ციკლი და პირობა.

# 19) შექმენით ფუნქცია analyze_sets, რომელიც მიიღებს ორ set-ს და დააბრუნებს tuple-ს ოთხი შედეგით:
#     - ყველა უნიკალური ელემენტი.
#     - საერთო ელემენტები.
#     - მხოლოდ პირველ set-ში არსებული ელემენტები.
#     - მხოლოდ ერთ-ერთ set-ში არსებული ელემენტები.












