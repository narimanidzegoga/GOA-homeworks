# 1) ახსენით რისთვის არის საჭირო ამდენი მონაცემთა ტიპები პროგრამირებაში?
# ეს მონაცემების ტიპები საჭიროა რადგან კომპიუტერმა სხვანაირად დაამუშავოს მონაცემები

# 2) მოიყვანეთ input-ისა და output-ის მაგალითები რეაულური ცხოვრებიდან
# input - მაგალითად, პულტზე ღილაკის დაჭერა - output - ტელევიზორზე არხის გადაცვლა
# input - შეკითხვის დასმა - output - პასუხის მიღება

# 3) შექმენით 1 სტრინგ ცვლადი, 1 ინტეჯერ ცვლადი და 1 ფლოატ ცვლადი. დაპრინტეთ მათი მონაცემთა ტიპები
name = "nikolozi"
print (type(name))
age =  25
print (type(age))
weight = 60.5
print (type(weight))
print (weight)
# 4) მომხმარებელს შემოაყვანინეთ მანძილი კილომეტრებში(დააფლოატეთ). დაპრინტეთ ეს მანძილი მეტრებში
distance = float(input("enter distance in kilometers: "))
print ("distance in meters is: ", distance * 1000)

# 5) მომხმარებელს მოთხოვეთ რაიმე ორი რიცხვი(დააინტეჯერეთ ორივე). დაპრინტეთ ყველა მათემატიკური ოპერაცია(+, -, *, /) ამ ორ რიცხს შორის
number1 = int(input("enter a number: "))
number2 = int(input("enter a second number: "))
print (number1 + number2)
print (number1 - number2)
print (number1 * number2)
print (number1 / number2)

# 6) შექმენით ე.წ. BMI Calculator(დასერჩეთ რო გაიგოთ რა არის). ფორმულა: წონა / სიმაღლე * სიმაღლე
weight = float(input("შეიყვანე წონა კგ-ში: "))
height = float(input("შეიყვანე სიმაღლე (მეტრებში): "))
bmi = weight / (height * height)
print ("your BMI is ",(int(bmi)))
