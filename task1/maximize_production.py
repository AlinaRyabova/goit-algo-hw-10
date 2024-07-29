import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += lemonade <= 50, "Sugar"
model += lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

model += lemonade + fruit_juice, "Total_Production"

model.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Статус розв'язку:", pulp.LpStatus[model.status])
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")