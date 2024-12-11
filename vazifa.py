from collections import namedtuple

# 1masala

# students = [
#     {'name': 'Ali', 'age': 20, 'major': 'Informatika'},
#     {'name': 'Vali', 'age': 22, 'major': 'Matematika'},
#     {'name': 'Gulnoza', 'age': 21, 'major': 'Fizika'}
# ]

# Talaba = namedtuple('Talaba', ['name', 'age', 'major'])

# for student in students:
#     talaba = Talaba(**student)
#     print(f"Ism: {talaba.name}, Yosh: {talaba.age}, Yo'nalish: {talaba.major}")

# ---------------------------------------------------------------------------------

# 2masala
# products = [
#     {'product_name': 'Olma', 'price': 5000, 'quantity': 10},
#     {'product_name': 'Banan', 'price': 8000, 'quantity': 5},
#     {'product_name': 'Uzum', 'price': 12000, 'quantity': 7}
# ]

# Mahsulot = namedtuple('Mahsulot', ['product_name', 'price', 'quantity'])

# for product in products:
#     mahsulot = Mahsulot(**product)
#     print(f"Mahsulot: {mahsulot.product_name}, Narxi: {mahsulot.price}, Miqdori: {mahsulot.quantity}")

# --------------------------------------------------------------------------------------

# 3masala
# cities = [
#     {'city_name': 'Toshkent', 'country': 'O‘zbekiston', 'population': 2500000},
#     {'city_name': 'Samarqand', 'country': 'O‘zbekiston', 'population': 500000},
#     {'city_name': 'Buxoro', 'country': 'O‘zbekiston', 'population': 300000}
# ]

# Shahar = namedtuple('Shahar', ['city_name', 'country', 'population'])

# eng_katta_shahar = max(cities, key=lambda city: city['population'])
# shahar = Shahar(**eng_katta_shahar)
# print(f"Eng katta aholi punktiga ega shahar: {shahar.city_name}, Aholisi: {shahar.population}")

# --------------------------------------------------------------------------------------

# 4masala

# cars = [
#     {'make': 'Chevrolet', 'model': 'Nexia', 'year': 2020},
#     {'make': 'Toyota', 'model': 'Camry', 'year': 2021},
#     {'make': 'Hyundai', 'model': 'Sonata', 'year': 2019}
# ]

# Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])

# eng_yangi_avtomobil = max(cars, key=lambda car: car['year'])
# avtomobil = Avtomobil(**eng_yangi_avtomobil)
# print(f"Eng yangi avtomobil: {avtomobil.make} {avtomobil.model}, Yili: {avtomobil.year}")

# --------------------------------------------------------------------------------------

# 5masala
# def outer_function():
#     def inner_function():
#         return "Bu ichki funksiya"
#     return inner_function

# closure = outer_function()
# print(closure())

# ----------------------------------------------------------------------------------------

# 6masala
# def greeting(name):
#     def inner_greeting():
#         return f"Salom, {name}!"
#     return inner_greeting

# salom = greeting("Ali")
# print(salom())


# ---------------------------------------------------------------------------------------

# 7masala

# def adder(x):
#     def inner_adder(y):
#         return x + y
#     return inner_adder

# add_five = adder(5)
# print(add_five(10))  

# ---------------------------------------------------------------------------------------

# 8masala
 
# def counter():
#     count = 0
#     def inner_counter():
#         nonlocal count
#         count += 1
#         return count
#     return inner_counter

# count = counter()
# print(count())  
# print(count())  
# print(count())  

# --------------------------------------------------------------------------------------------

# 9masala
# def square():
#     def inner_square(x):
#         return x * x
#     return inner_square

# kvadrat = square()
# print(kvadrat(4))  

# -----------------------------------------------------------------------------------------------

# 10masala
# def name_list():
#     names = []
#     def inner_name_list(name):
#         names.append(name)
#         return names
#     return inner_name_list

# add_name = name_list()
# print(add_name("Ali"))  
# print(add_name("Vali"))  

# -------------------------------------------------------------------------------------------------

# 11masala

# def discount(discount_percent):
#     def inner_discount(price):
#         return price * (1 - discount_percent / 100)
#     return inner_discount

# chegirma = discount(10)
# print(chegirma(100000))  

# --------------------------------------------------------------------------------------------------

# 12masala

# def multiplier():
#     product = 1
#     def inner_multiplier(x):
#         nonlocal product
#         product *= x
#         return product
#     return inner_multiplier

# multiply = multiplier()
# print(multiply(2))  
# print(multiply(3))  
# print(multiply(4))  

# ---------------------------------------------------------------------------------------------------

# 13masala
# def string_adder():
#     result = ""
#     def inner_string_adder(s):
#         nonlocal result
#         result += s
#         return result
#     return inner_string_adder

# add_string = string_adder()
# print(add_string("Hello"))  
# print(add_string(" World"))  

# -----------------------------------------------------------------------------------------------------

# 14masala
# def odd_filter():
#     def inner_odd_filter(numbers):
#         return [num for num in numbers if num % 2 != 0]
#     return inner_odd_filter

# filter_odd = odd_filter()
# print(filter_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))  

# -----------------------------------------------------------------------------------------------------

# 15masala
# def exponent(n):
#     def inner_exponent(x):
#         return x ** n
#     return inner_exponent

# square = exponent(2)
# print(square(4))

# cube = exponent(3)
# print(cube(2))  

# ----------------------------------------------------------------------------------------------------

# 16-masala
# def reverse_string():
#     def inner_reverse_string(s):
#         return s[::-1]
#     return inner_reverse_string

# reverse = reverse_string()
# print(reverse("Hello"))  

# -----------------------------------------------------------------------------------------------------

# 17-masala
# def shopping_cart():
#     cart = []
#     def inner_shopping_cart(product, price):
#         cart.append((product, price))
#         total = sum(item[1] for item in cart)
#         return cart, total
#     return inner_shopping_cart

# savat = shopping_cart()
# print(savat("Olma", 5000))  
# print(savat("Banan", 8000))  

# -----------------------------------------------------------------------------------------------------

# 18-masala

# def price_list():
#     prices = []
#     def inner_price_list(price):
#         prices.append(price)
#         return prices
#     return inner_price_list

# add_price = price_list()
# print(add_price(5000))  
# print(add_price(8000))  

