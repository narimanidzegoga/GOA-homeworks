#1) გაიხსენეთ ყველა ნასწავლი მონაცემთა ტიპი და თითოეულისათვის შექმენით 5 ცვლადი
# int - მთელი რიცხვი
age = 25
height = 180
score = 10
temperature = 2
weight = 65
# float - ათწილადი რიცხვი
height_in_meters = 1.7
distance = 4.5
price = 19.99
length = 15.5
speed = 45.8
# string - ბრჭყალებში მოცემული ნებისმიერი სიმბოლო
name ="nika"
last_name =""
city = "tbilisi"
color = "orange"
country = "georgia"

# 2) ახსენით რა არის ოპერატორი და რამდენი ტიპის ოპერატორი ისწავლეთ, მოიყვანეთ თითოეულისათვის რამე მაგალითი
# სიმბოლო რომელიც ცვლადებზე ან მნიშვნელობებზე მოქმედებას ასრულებს
# არითმეტიკული ოპერატორები
a = 20
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)
# შედარების ოპერატორები
print(5 > 3)
print(2 < 1)
print(7 >= 7)
print(4 <= 2)
# ლოგიკური ოპერატორები
battery = 80
is_full = battery > 70
print(is_full)

temperature = 15
is_cold = temperature <= 10
print(is_cold)

is_weekend = False
is_holiday = True
can_rest = is_weekend and is_holiday
print(can_rest)  # False

is_sunny = False
is_warm = True
can_go_outside = is_sunny or is_warm
print(can_go_outside)

#3) დაწერეთ დღეს მიერ ნასწავლ შედარების ოპერატორებზე ხუთ ხუთი მაგალითი
# > - მეტობა
print(5 > 3)
print(10 > 20)
print(7 > 7)
print(100 > 50)
print(0 > -1)
# < - ნაკლებბობა
print(3 < 5)
print(20 < 10)
print(7 < 7)
print(50 < 100)
print(-1 < 0)
# >= - მეტია ან უდრის
print(5 >= 3)
print(7 >= 7)
print(10 >= 20)
print(100 >= 50)
print(0 >= 1)
# <= - ნაკლებია ან ტოლია
print(3 <= 7)
print(5 <= 5)
print(10 <= 2)
print(-4 <= 0)
print(8 <= 3)

#4) ახსენით რა არის boolean და რომლებია მისი მნიშვნელობები
# boolean - ეს არის მონაცემის ტიპი რომელსაც შეიძლება ჰქონდეს 2 მნიშვნელობა - true - სიმართლე, ან false - სიცრუე

#5) მომხმარებელს შემოატანინე ორი რიცხვი. შეამოწმე არის თუ არა პირველი რიცხვი მეტი მეორეზე
a = float(input("შეიყვანეთ პირველი რიცხვი: "))
b = float(input("შეიყვანეთ მეორე რიცხვი: "))
is_first_greater = a > b
print("პირველი რიცხვი მეტია მეორეზე?", is_first_greater)

#6) მომხმარებელს შემოატანინე ორი რიცხვი. შეამოწმე არის თუ არა პირცელი რიცხვი მეტი 10 ზე. შეამოწმე არის თუ არა მეორე რიცხვი მეტი 20 ზე
first_number = float(input("შეიყვანეთ პირველი რიცხვი: "))
second_number = float(input("შეიყვანეთ მეორე რიცხვი: "))
is_first_over_10 = first_number > 10
is_second_over_20 = second_number > 20
print("პირველი რიცხვი მეტია 10-ზე?", is_first_over_10)
print("მეორე რიცხვი მეტია 20-ზე?", is_second_over_20)

#7) მომხმარებელს შემოატანინე რიხვი. შეამოწმე არის თუ არა ეს რიცხვი 100 დან 999 ის ჩათვლით შუალედში
number = int(input("შეიყვანეთ რიცხვი: "))
result = 100 <= number <= 999
print("რიცხვი 100-დან 999-მდეა?", result)