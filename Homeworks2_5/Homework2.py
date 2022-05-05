# 1 of 15
is_next = None
num = int(input("Введите количество баллов: "))
if num >= 83:
  #print("You've passed the interview")
  is_next = True
else:
  is_next = False
print(is_next)
    
# 2 of 15
is_active = bool(input("Пользователь активен? "))
is_admin = bool(input("Пользователь администратор? "))
is_permission = bool(input("Пользователь имеет доступ? "))
if is_admin: 
  access = True
elif is_active and is_permission:
  access = True
else:
  access = False
print(access)

# 3 of 15
work_experience = int(input("Введите свой стаж полных лет: "))
if 1 < work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"
print(developer_type)

# 4 of 15
num = int(input("Введите число: "))
if num > 0:
    if num % 2:
        result = "Положительное нечетное число"
    else:
        result = "Положительное четное число"
elif num < 0:
    result = "Отрицательное число"
else:
    result = "Это ноль"
print(result)

# 5 of 15
import math
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    print(x1)
else:
    print("Нет решений")

# 6 of 15
num = int(input("Введите целое число: "))
is_even = True if num % 2 == 0 else False

# 7 of 15
num = int(input("Введите целое число (0 до 100): "))
sum = 0
count = 0
while count < num:
    count += 1
    sum += (count +1)
print(sum)

# 8 of 15
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    if char == search:
        result += 1    
print(result)

# 9 of 15
first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
if first <= second:
    nod = first
else:
    nod = second
while first % nod != 0 or second % nod != 0:
    nod = nod - 1
print(nod)   

# 10 of 15
num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while num != 0:
  for ch in range(num + 1):
    sum += ch
  num = int(input("Введите целое число (0 для выхода): "))
print(sum)

# 11 of 15
num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while True:
    for ch in range(num + 1):
        sum += ch
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
print(sum) 

# 12 of 15
num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while True:
    if num == 0:
        break
    for ch in range(num + 1):
        if ch % 2 == 1:
            continue
        sum += ch
    num = int(input("Введите целое число (0 для выхода): "))   
print(sum) 

# 13 of 15
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
encoded_ch = ""
for ch in message:
    if ch.islower():
        pos = ord(ch) - ord('a') 
        pos = (pos + offset) % 26 
        encoded_ch = chr(pos + ord("a"))
    elif ch == ' ':
        encoded_ch = ' '
    elif ch == '!':
        encoded_ch = '!'
    else:
        pos = ord(ch) - ord('A') 
        pos = (pos + offset) % 26 
        encoded_ch = chr(pos + ord("A"))        
    encoded_message += encoded_ch
print(encoded_message)

# 14 of 15
pool = 1000
quantity = int(input("Введите количество рассылок: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Выполнено деление на ноль!')
else:
    print(f"Надо отправить {chunk} sms")
finally:
    print("Thank you!")

# 15 of 15
result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input('Enter Numbers and Operators: ')
    
    if user_input == "=":
            print(f'Your result is {result}. \nThank you for coming!')
            break
    
    if wait_for_number:
        try:
            operand = float(user_input)
            print(f'You\'ve entered the number {operand}, Thx! \n')
        except ValueError:
            print ('Enter the Number, please. Try again!\n')
            continue
        
        wait_for_number = False
        
        if not result:
            result = operand

        else:
            if operator == '+':
                result = result + operand
            elif operator == '-':
                result = result - operand
            elif operator == '*':
                result = result * operand
            elif operator == '/':
                result = result / operand    
    else:
        if user_input in ('+', '-', '*', '/'):
            operator = user_input
            print(f'You\'ve entered the Operator "{operator}", THX\n')
        else:
            operator = None
        
        if not operator:    
            print('Enter Operator, please!')    
        else:
            wait_for_number = True

#Первая: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "="], результат 18.0
#Вторая: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0