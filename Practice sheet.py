import math
pi = 23.56
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(pi))
print(abs(pi))
print(pow(pi, 2))
x = 1
y = 2
z = 3
print(max(x,y,z))
print(min(x,y,z))

while True:
    name = input("enter your name: ")
    if name != "":
        break

phone_number = "015-1613-5782"
for i in phone_number:
    if i == "-":
       continue

    print (i, end="")

for i in range (1,21):
    if i == 13:
        pass
    else:
        print(i)

food = ["pizza", "coffee", "ice cream"]
food.sort()
food[0] = "sushi"
print(food)
print(food[0])
food.append("pie")
for x in food:
    print(x)

dinner = ["chicken", "rice", "curry"]
lunch = ["veg", "soup"]
breakfast = ["egg", "banana"]

food = [dinner,lunch, breakfast]
print(food)
print(food[0][0])
