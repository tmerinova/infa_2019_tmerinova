
i = 0

while i < 10:

    if i == 3:
        i += 1
        continue
    print(i)

    if i == 5:
        break

    i += 1

    print()
    print()

my_list = [1, 2, 4, 5]

for i in my_list:
    if i == 7:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")


for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} делится на 3, результат {int(quotient)}.")


for i in reversed(range(5)):
    print(i)


def keyword_function(a=1, b=2):
    return a + b


print(keyword_function(6, 9))


def many(*args, **kwargs):
    print(args)
    print(kwargs)


many(1, 2, 3, name="Mike", job="programmer")




