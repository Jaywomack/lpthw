def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

odd_names = list(map(splicer, names))
print(odd_names)


def check_even_nums(num):
    return num % 2 == 0


even_nums = list(filter(check_even_nums, my_nums))
print(even_nums)

odd_nums = list(filter(lambda num: num % 2 != 0, my_nums))
print(odd_nums)

odds_times_five = list(map(lambda num: num * 5, odd_nums))
print(odds_times_five)