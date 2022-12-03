try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("we have an NameError")
except ZeroDivisionError:

        print("we have an ZeroDivisionError")

print("code after capsule")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print("start code")
    print(10 / 0)
    print("no error")
except(NameError, ZeroDivisionError) as error:
    print(error)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    try:
        print("start code")
        print(error)
        print("no errors")
    except SyntaxError:
        print("wrong syntax")
except NameError as pasha:
        print(pasha)
try:
        print("start code")
        print(pasha)
        print("no errors")
except NameError as pasha:
        print(pasha)

else:
    print("I am ELSE") #якщо немає помилки
finally:
    print("КОНЕЦ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def checker(var_1):
    if type(var_1) != str:
        raise TypeError (f'Soory, we can t work with {type(var_1)}',f'we need class str')
    else:
        return var_1
print(checker(10))
my_list = [1, 2, 3, 4, 5]
for i in range(1, 10):
    iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
