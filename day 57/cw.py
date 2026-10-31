# 1) შექმენით დიქთი, სადაც შეინახავთ ინფორმაციას კოსმოსური ხომალდის შესახებ
#   - დაპრინტეთ ამ კოსმოსური ხომალდის რაიმე მნიშვნელობა
#   - შეცვალეთ ამ კოსმოსური ხომალდის რაიმე გასაღების მნიშვნელობა
#   - დაამატეთ ამ კოსმოსურ ხომალდში რაიმე item
#   - წაშალეთ ამ კოსმოსური ხომალდიდან რაიმე item

spacecraft = {
    "name": "Rocket",
    "color": "white",
    "country": "USA"
}
print(spacecraft["name"])
spacecraft["color"] = "black"
spacecraft["speed"] = 1000
del spacecraft["country"]
print(spacecraft)


# 2) გამოიყენეთ წინა დავალებაში არსებული დიქთი. ფორ ლუპის საშუალებით დაპრინტეთ:
#   - მისი ყველა მნიშვნელობა ცალკ ცალკე
#   - მისი ყველა გასაღები ცალკ ცალკე 
#   - მისი ყველა item ცალკ ცალკე    

values = spacecraft.values()
keys = spacecraft.keys()
items = spacecraft.items()

for value in values:
    print(value)

for key in keys:
    print(key)

for item in items:
    print(item)