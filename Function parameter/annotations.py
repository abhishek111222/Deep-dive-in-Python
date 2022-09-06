#Sphinx generates documentation from your code.

x = 3
y = 5


def my_func(a : str) -> 'a repeated ' + str(max(x, y)) + ' times':
    return a* max(x, y)




#print(help(my_func))
print(my_func.__annotations__)