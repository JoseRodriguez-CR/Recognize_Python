num1 = 42   #variable declaration,   Data Types,   Primitive,   numbers
num2 = 2.3   #variable declaration,   Data Types,    Primitive,   numbers
boolean = True   #variable declaration,    Data Types,   Primitive,   boolean
string = 'Hello World'   #variable declaration,     Data Types,      Primitive,     string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration,   list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#variable declaration,    dictionary
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration,     tuple
print(type(fruit))  #access value
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms')  #add value
print(person['name'])   #access value
person['name'] = 'George'   #change value
person['eye_color'] = 'blue'    #add value
print(fruit[2]) #access value

if num1 > 45:   #if
    print("It's greater")
else:   #else
    print("It's lower")

if len(string) < 5: #if
    print("It's a short word!")
elif len(string) > 15:  #else if
    print("It's a long word!")
else:   #else
    print("Just right!")

for x in range(5):  #for, start
    print(x)    #stop
for x in range(2,5):    #for, start
    print(x)    #stop
for x in range(2,10,3): #for, start
    print(x)    #stop
x = 0   #while
while(x < 5):   #start
    print(x)
    x += 1  #stop

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""                     #comment in multiple line
Bonus section           #comment in multiple line
"""                     #comment in multiple line

# print(num3)                         #commentin single line
# num3 = 72                           #commentin single line
# fruit[0] = 'cranberry'              #commentin single line
# print(person['favorite_team'])      #commentin single line
# print(pizza_toppings[7])            #commentin single line
#   print(boolean)                    #commentin single line
# fruit.append('raspberry')           #commentin single line
# fruit.pop(1)                        #commentin single line

