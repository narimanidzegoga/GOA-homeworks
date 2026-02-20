# ეს მონაცემების ტიპები საჭიროა რადგან კომპიუტერმა სხვანაირად დაამუშავოს მონაცემები
# input - მაგალითად, პულტზე ღილაკის დაჭერა - output - ტელევიზორზე არხის გადაცვლა
# input - შეკითხვის დასმა - output - პასუხის მიღება
name = "nikolozi"
print (type(name))
age =  int(25)
print (type(age))
weight = float(60.5)
print (type(weight))

distance = float(input("enter distance in kilometers: "))
print ("distance in meters is: ", distance * 1000)
number1 = int(input("enter a number: "))
number2 = int(input("enter a second number: "))
print (number1 + number2)
print (number1 - number2)
print (number1 * number2)
print (number1 / number2)
#6) შექმენით ე.წ. BMI Calculator(დასერჩეთ რო გაიგოთ რა არის). ფორმულა: წონა / სიმაღლე * სიმაღლე
weight = float(input("შეიყვანე წონა კგ-ში: "))
height = float(input("შეიყვანე სიმაღლე (მეტრებში): "))
bmi = weight / (height * height)
print ("your BMI is ",(int(bmi)))
