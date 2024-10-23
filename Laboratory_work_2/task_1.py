money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

no_debts_month_count = 0 #Число месяцев без долгов
budget_for_month = money_capital + salary  #Общее состояние

while(budget_for_month - spend > 0):
    budget_for_month += (salary - spend)
    spend += (spend * increase)
    no_debts_month_count += 1


print("Количество месяцев, которое можно протянуть без долгов:", no_debts_month_count)
