# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now : ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)


numbers = []


def iterator(start, finish, step):
    for i in range(start, finish, step):
        numbers.append(i)
        i += step
        if i > finish:
            break


iterator(0, 125, 25)
print(numbers)
