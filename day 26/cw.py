# 1)შექმენით სია , სადაც გექნებათ ნებისმიერი ტიპის ელემენტები მინიმუმ 5 ელემენტი , შემდეგ:
#   1)ამ სიაში დაამატე ახალი ელემენტი ბოლოში
#   2)ჩასვი რიცხვი 8 მე3 ინდექსზე
#   3)წაშალე მეორე ელემენტი
#   4)ამოიღე ბოლო ელემენტი და შეინახე ცალკე ცვლადში და დაბეჭდე
#   5)შეატრიალე სია
#   6)ბოლოს დაბეჭდე

my_list = [10 , "goga" , 15 , True , 20 , "nika"]
my_list.append("new element")
my_list.insert(3, 8)
my_list.remove("goga")

last_element = my_list.pop(-1)
print(last_element)
my_list.reverse()
print(my_list)




# 2)მომხარებელს შეაქმნევინეთ სია , გამოიყენეთ ინფუთები
my_list = []

for i in range(5):
    users_input = input("enter anything: ")
    my_list.append(users_input)

print(my_list)




