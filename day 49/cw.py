# 1) შექმენით ორი სეტი. თითოეულში შეინახეთ რანდომ ელემენტები.
#   - გამოიყენეთ დღეს ნასწავლი ოთხივე მეთოდი და თან ოთხივე ახსენით კომენტარით
#   - ოთხივე მეთოდის შედეგი დაპრინტეთ
#   - დაპრინტეთ ორივე სეტი კოდის ბოლოს
set1 = {4, 17, 28, 63, 90}
set2 = {17, 35, 63, 88, 101, 120}

# intersection() - აბრუნებს იმ ელემენტებს, რომლებიც ორივე სეტშია
intersection_set = set1.intersection(set2)
# union() - აბრუნებს ყველა უნიკალურ ელემენტს ორივე სეტიდან
union_set = set1.union(set2)
# difference() - აბრუნებს ელემენტებს, რომლებიც მხოლოდ პირველ სეტშია
difference_set = set1.difference(set2)
# symmetric_difference() - აბრუნებს ელემენტებს, რომლებიც მხოლოდ ერთ-ერთშია
symmetric_difference_set = set1.symmetric_difference(set2)
print(intersection_set, "intersection")
print(union_set, "union")
print(difference_set, "difference")
print(symmetric_difference_set, "symmetric difference")
print(set1, "set1")
print(set2, "set2")