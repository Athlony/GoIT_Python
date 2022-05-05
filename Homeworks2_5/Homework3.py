

#3 of 11
base_rate = 40
price_per_km = 10
total_trip = 0
all_price = 0

def trip_price(path):
    global total_trip
    all_price = base_rate + price_per_km * path
    if all_price >= 40:
        total_trip += 1
    print(all_price)
    return all_price
    return total_trip

trip_price(10)
print(all_price, total_trip)

#4 of 11
def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        price = price - (price * discount)

    apply_discount()
    print(price)
    return price

discount_price(100, 0.1)

#5 of 11
def get_fullname(first_name, last_name, middle_name = None):
    print (first_name, middle_name, last_name)
    if middle_name == None:
        return first_name + ' ' + last_name
    else:
        return first_name + ' ' + middle_name + ' ' + last_name

print(get_fullname(first_name = 'Anton', last_name = 'Yemets'))

#6 of 11
def format_string(string, length):
    space = ' '
    if len(string) >= length:
        return string
    elif len(string) < length:
        string = (space * int((length - len(string)) // 2)) + string
        return string

#format_string(aaaaaaaaaaaaaaaaac', length=12)
print(format_string(length=15, string='abaa'))

#7 of 11
def first(size, *args):
    size = size + int(len(args))
    return size

print(first(5, "first", "second", "third"))
print(first(1, "Alex", "Boris"))

def second(size, **kwargs):
    size = size + int(len(kwargs))
    return size

print(second(3, comment_one="first", comment_two="second", comment_third="third"))
print(second(10, comment_one="Alex", comment_two="Boris"))

#8 of 11
def cost_delivery(quantity, *_, discount = 0.0):
    if discount == 0.0:
        result = 5 + (int(quantity - 1) * 2)
    else:    
        result = (5 + (int(quantity - 1) * 2)) * discount
    return result

print(cost_delivery(2, 1, 2, 3, discount=0.5))

#9 of 11
def cost_delivery(quantity, *_, discount = 0.0):
    """
    Функция возвращает общую сумму доставки.

    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.
    """
    if discount == 0.0:
        result = 5 + (int(quantity - 1) * 2)
    else:    
        result = (5 + (int(quantity - 1) * 2)) * discount
    return result

print(cost_delivery(2, 1, 2, 3, discount=0.5))

#10 of 11
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)    

def number_of_groups(n, k):
    result = int(factorial(n) / (factorial(n-k) * factorial(k)))
    return result

print(number_of_groups(50, 7))

#11 of 11
def fibonacci(n):
    if(n <= 1): 
        return n 
    else: 
        result = (fibonacci(n-1) + fibonacci(n-2))
        return result

print("Fibonacci:", fibonacci(10))