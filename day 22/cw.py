#   1) შექმენით სტრინგი 'airplane' და ააწტვეთ სიტყვა rain როგორც დადებითი ინდექსებით ისე უარყოფითი ინდექსებით
word = "airplane"

rain = word[2] + word[0] + word[1] + word[6]
print(rain)
rain = word[-6] + word[-8] + word[-7] + word[-2]

print(rain)