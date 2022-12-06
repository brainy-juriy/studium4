def simple_separator():
    result = ('**********')
    return('**********')
print(simple_separator() == '**********')



def long_separator():
    num_ = int(input('введите число:'))
    count = ('*' * num_)
    return count
print(long_separator())




def long_separator(x):
    count = ('*' * x)
    return count
long_separator(4)
print(long_separator(4))

long_separator(25)
print(long_separator(25))





def separator(x, y):
    result = x * y
    return result

print(separator(10, '-'))

print(separator(5, '#'))





def hello_world():
    print('*' * 11)
    print('Hello world!')
    print('#' * 11)
print(hello_world())






def hello_who(who = 'World'):
    print('*' * 10)
    print(f'Hello, {who}!')
    print('#' * 10)

hello_who()
hello_who('John')
hello_who('Sandra')








def pow_many(power, *args):
    z = ((sum(args)**power))
    return z


print(pow_many(1,1,2))      # 3
print(pow_many(1,2,3))      # 5
print(pow_many(2,1,1))      # 4
print(pow_many(3,2))        # 8
print(pow_many(2,1,2,3,4))  # 100








def print_key_val(**kwargs):
    for k,v in kwargs.items():
        print(k)
        print(v)

print_key_val( name = 'name --> Max', age = str('age --> 21'))
print_key_val(animal ='animal --> Cat', is_animal = 'is_animal --> True')









numbers = [1, 2, 3, 4, 5]
result = []

def my_filter(iterable, function):
    for i in numbers:
        if function(i) is True:
            result.append(i)
        else:
            return False
    print((list(result)))

my_filter([1, 2, 3, 4, 5], lambda i: i > 3)