#01 of 14
from time import CLOCK_PROCESS_CPUTIME_ID


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:        
            sum = sum + value
        else:
            continue
    return sum
print(amount_payment([1, -3, 4]))

#02 of 14
def prepare_data(data):
    
    data.remove(max(data))
    data.remove(min(data))
    data.sort()
    return data

#03 of 14
def format_ingredients(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]
    new =''
    for s in items[:-2]:
        new += s + ', '
    return new + items[-2] + ' и ' + items[-1]

#04 of 14
def get_grade(key):
    grades = {
        'F': 1,
        'FX': 2, 
        'E': 3,
        'D': 3,
        'C': 4,
        'B': 5,
        'A': 5
    }
    print(grades.get(key, None))
    return grades.get(key, None)

def get_description(key):
    grades = {
        'F': 'неудовлетворительно',
        'FX': 'неудовлетворительно', 
        'E': 'достаточно',
        'D': 'удовлетворительно',
        'C': 'хорошо',
        'B': 'очень хорошо',
        'A': 'отлично'
    }
    return grades.get(key, None)

    #05 of 14
    def lookup_key(data, value):        
        result = list()
        for key, val in data.items():
            print(key, val)
            if val == value:
                result.append(key)
        return result    

#06 of 14
grade1 = [1, 12, 3, 24, 5]
def split_list(grade):
    sum = 0
    high = []
    low = []

    for i in grade:
        sum = sum + i
    # print(sum)
    # print(sum / len(grade))

    for i in grade:   
        if i > (sum / len(grade)):
            high.append(i)
        else:
            low.append(i)
    
    result = (low, high)
    return result
    
print(split_list(grade1))

#07 of 14
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0
    result = 0
    for i in range(0, (len(coordinates) - 1)):
        x = coordinates[i]
        y = coordinates[i + 1]
        if x > y:
            x, y = y, x
        route = (x, y)
        
        for keys, vals in points.items():
            if keys == route:
                result = result + vals

    return result

coordinates1 = [0, 1, 3, 2, 0]
print(calculate_distance(coordinates1))

#08 of 14
def game(terra, power):
    for lists in terra:
        for points in lists:
            if points <= power:
                power = power + points
            else:
                break                
    return power    
 
terra1 = [[1, 1, 6, 10], [10, 2], [1, 1, 1]]
power1 = 4
print(game(terra1, power1))

#09 of 14
def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0 or len(pin_codes) > len(set(pin_codes)):
        return False

    for pins in pin_codes:
        for ch in pins:
            if ch not in "0123456789":
                return False

        if len(pins) != 4:
            return False

        if type(pins) != str:
            return False

    return True
        

pin_codes1 = ['1101', '903', '0011', '1101']
print(is_valid_pin_codes(pin_codes1))

#10 of 14
from random import randint

def get_random_password():
    password = ''
    while True:
        random_num = randint(40, 126)
        password = password + chr(random_num)
        if len(password) == 8:
            break
    return password

print(get_random_password())

#11 of 14
def is_valid_password(password):

    check = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in password:
        if ch in "0123456789":
            check += 1
            break
    for ch in password:    
        if ch in alphabet:
            check += 1
            break
    for ch in password:    
        if ch in alphabet.upper():
            check += 1
            break
    print(check)
    if len(password) == 8 and check == 3:
        return True
    else:
        return False

print(is_valid_password(get_random_password()))

#12 OF 14
from random import randint
from unittest import result


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    while True:
        password = get_random_password()
        #print(password)
        valid_password = is_valid_password(password)
        if valid_password == True:
            return password
        else:
            False

print(get_password())

#13 of 14
from pathlib import Path
def parse_folder(path):
    files = []
    folders = []
    #path = Path(path)
    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        if i.is_dir():
            folders.append(i.name)
 
    return files, folders
 
print(parse_folder('/Users/athlony/Desktop/Python'))      

#14 of 14
import sys

def parse_args():
    result = ""
    for arg in sys.argv[1:]:
        result = result + arg 
        result = result + ' '
           
    return result[:-1]

print(parse_args())