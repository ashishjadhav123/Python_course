

# def my_fun(*args):
#     print(args[1])
#
# my_fun(1,3,5,8)


def myfunc(in_str):
    str1 = ''
    for i in range(len(in_str)):
        if i % 2 == 0:
            str1 = str1 + str(in_str[i]).lower()
        else:
            str1 = str1 + str(in_str[i]).upper()

    return str1


# data = myfunc('Anthropomorphism')
# print(data)

# -------------- Map function ------------------

def square(list_val):
    return list_val**2

list1 = [1,2,3,4,5,6]

print(list(map(square,list1)))

# -------------- Filter function ------------------

def mod_fun(list_val):
    return list_val%2 == 0

list1 = [1,2,3,4,5,6]

print(list(filter(mod_fun,list1)))

# -------------- Lambda function ------------------

lambda_square = lambda x: x**2

print(lambda_square(2))
