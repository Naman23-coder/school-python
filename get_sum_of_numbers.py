a = 1
b = 2
c = a + b
print('the sum of a and b is', c)

# alternative method
# using f strings
print(f'the sum of a and b is {c}')

# alternative method
# using format method
print('the sum of a and b is {}'.format(c))

# alternative methods
# using + method
# str method changes integer,float etc. types of data types to string format
print('the sum of a and b is ' + str(c))
