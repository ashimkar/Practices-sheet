import random
x = random.randint(1,6)
y = random.random()
print(y)


my_list = ["rock", "paper", "scissors"]
z = random.choice(my_list)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"j", "q", "k", "a"]
random.shuffle(cards)
print(cards)

number = 3.120205
print("the number pi is {:.2f}".format(number))
print("the number is {:,}".format(number))

name = "ashim"
print("hello, my name is {}".format(name))
print("hello, my name is {:10}. nice to meet you".format(name))

animal = "cow"
item = "moon"
print("the "+ animal + " jumped over the "+ item)
print("the {} jumped over the {}".format(animal,item))
print("the {1} jumped over the {0}".format(animal,item))
print("the {0} jumped over the {0}".format(animal,item))

text = "the {} jumped over the {}"
print(text.format(animal,item))

def hello(first, last):
    print("hello " + first + " " + last)

hello(first="ashim", last="kar")

def hello(**kwargs):
    print("hello ", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title= "mr.", first="ashim", middle=" c ", last="kar")

def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(1,2))

def add (*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3))

name = "ashim"
def display_name():
    name = "kar"
    print(name)
display_name()
print(name)

num = input("enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
#print(num)

#print(abs(round(float(input("enter a whole positive number: ")))))

#def hello (name,age):
   # print("hello " + name)
  #  print("you are " + str(age) + " years old")
  #  print("how're you doing?")
#name = "ash"
#age = 26
#hello(name, age)


def multiply (number1,number2):
    result = number1 * number2
    return result
print(multiply (6,8))

def hello (first, middle, last):
    print("hello "+ first+ " " + middle  + " " + last)
hello("mr.", "ashim", "kar")
hello(last= "mr.",middle= "ashim",first= "kar")
