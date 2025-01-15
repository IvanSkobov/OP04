#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%.
#Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(a, years):
    total_amount = a


    interest_rate = 0.10

    for year in range(years):
        total_amount += total_amount * interest_rate

    return total_amount

initial_deposit = float(input("Введите сумму вклада (в рублях): "))
investment_years = int(input("Введите срок вклада (в годах): "))
final_amount = bank(initial_deposit, investment_years)

income = final_amount - initial_deposit

print("Ваш доход по депозиту за", investment_years, "лет составит:", round(income, 2), "рублей.")
print("Сумма на счету через", investment_years, "лет составит:", round(final_amount, 2), "рублей.")