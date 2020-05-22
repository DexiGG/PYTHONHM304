# 1
question = int(input('введите еденицу измерения'
                     '1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер'))
mass = int(input('введите массу'))
if question == 2:
    val = mass / 1000000
    print(val, 'кг')
if question == 3:
    val = mass / 1000
    print(val, 'кг')
if question == 4:
    val = mass * 1000
    print(val, 'кг')
if question == 5:
    val = mass * 100
    print(val, 'кг')

# 2
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number * number)
print(squares)


# 3
def expt(b, n):
    if n == 0:
        return 1
    return b * expt(b, n - 1)

