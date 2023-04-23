print(1 + 2)

print(10/5)

print(10*3)

print('Hello my name is {}'.format('Ashish'))

print('Hello my name is {0}, I am from {2}, I want to become {1}'.format('Ashish','India', 'Data Engineer'))

result = 100/777

print("Result is : {r:1.4f}".format(r=result))

# List comprehensions

even_num = [num for num in range(0, 11) if num % 2 == 0]
print(even_num)

num_list = [num if num % 2 == 0 else 'odd' for num in range(0, 11)]
print(num_list)

two_list = [x * y for x in [1,2,3] for y in [1,10,100]]
print(two_list)
