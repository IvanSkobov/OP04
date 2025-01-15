#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.

def sum_range(start, end):
    if start > end:
        return "Ошибка: начальное значение больше конечного."

    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start = int(input("Введите начальное значение: "))
end = int(input("Введите конечное значение: "))
result = sum_range(start, end)
print("Сумма всех целых чисел от", start, "до", end, "включительно: = ", result)

