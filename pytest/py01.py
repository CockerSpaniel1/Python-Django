coffee="美式咖啡"
price=50
qty=10

print("咖啡:",coffee)
print("價格:",price)
print("數量:",qty)

discount1 = 45
discount2 = price * 0.9

if discount1 < discount2:
    print("折扣一比較划算")
if discount1 > discount2:
    print("折扣二比較划算")
if discount1 == discount2:
    print("兩者都不划算")

if discount1 < discount2:
    print("折扣一比較划算")
else:
    print("折扣二比較划算")


if discount1 < discount2:
    print("折扣一比較划算")
elif discount1 == discount2:
    print("兩者都不划算")
else:
    print("折扣二比較划算")

for i in range(10):
    print(i)
print("----------------------------------")
for i in range(1,10):
    print(i)
