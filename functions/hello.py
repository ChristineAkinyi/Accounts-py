def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    year = 2024-age
    print(f"Hello {name}, you were born in {year}")  

def my_country (country="Uganda"):
    print(f"Hello AKiraChix from {country}")  

# def numbers():
#     list_number = []
#     for number in range(2000,3201):
#         if number%7 == 0 and number%5 != 0:
#            list_number.append(number)
#         print(list_number)

# numbers()

# def integral (n):
#     my_dict = {}
#     for number in range(1, n+1):
#         my_dict[number] = number*number
#     return(my_dict)

# print(integral(8))

def greet (*names):
    """hello"""
    for name in names:
        print(f"Hello {name}")

def create_sentence(**words):
    """hello"""
    print(words)
    sentence =""
    for word in words.values():
        sentence += word
        sentence+= " "
    return sentence

def sum_and_greet(*args, **kwargs):
    """hello"""
    total =0
    for x in args:
        total += x
    f = kwargs["first_name"]
    l = kwargs["last_name"]
    greeting = f"Hello {f} {l}, total of your numbers is {total}"
    return greeting