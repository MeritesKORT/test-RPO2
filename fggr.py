start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

sum_even = 0  # сумма четных чисел
count_even = 0  # количество четных чисел

sum_odd = 0   # сумма нечетных чисел
count_odd = 0  # количество нечетных чисел

sum_nine = 0  # сумма чисел, кратных 9
count_nine = 0  # количество чисел, кратных 9

for num in range(start, end + 1):
    if num % 2 == 0:
        sum_even += num
        count_even += 1
    else:
        sum_odd += num
        count_odd += 1
    if num % 9 == 0:
        sum_nine += num
        count_nine += 1

if count_even != 0:
    avg_even = sum_even / count_even
else:
    avg_even = None

if count_odd != 0:
    avg_odd = sum_odd / count_odd
else:
    avg_odd = None

if count_nine != 0:
    avg_nine = sum_nine / count_nine
else:
    avg_nine = None

print(f"Сумма четных чисел: {sum_even}, Среднее арифметическое четных чисел: {'%.2f' % avg_even if avg_even is not None else 'нет четных чисел'}")
print(f"Сумма нечетных чисел: {sum_odd}, Среднее арифметическое нечетных чисел: {'%.2f' % avg_odd if avg_odd is not None else 'нет нечетных чисел'}")
print(f"Сумма чисел, кратных 9: {sum_nine}, Среднее арифметическое чисел, кратных 9: {'%.2f' % avg_nine if avg_nine is not None else 'нет чисел, кратных 9'}")

length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")

for _ in range(length):
    print(symbol)

while True:
    num = int(input("Введите число: "))
    if num > 0:
        print("Число положительное")
    elif num < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")
        break
print("Good bye!")

numbers = []  # список для хранения всех введённых чисел

while True:
    num = int(input("Введите число: "))
    if num == 7:
        break
    numbers.append(num)

if numbers:
    total_sum = sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"Сумма чисел: {total_sum}")
    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")
else:
    print("Вы не ввели ни одного числа кроме 7.")

print("Good bye!")
