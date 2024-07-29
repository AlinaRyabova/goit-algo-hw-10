Опис домашнього завдання Завдання 1. Оптимізація виробництва

Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Для виробництва
цих напоїв використовуються різні інгредієнти та обмежена кількість обладнання.
Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.

Умови завдання:

"Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку". "Фруктовий сік"
виготовляється з "Фруктового пюре" та "Води". Обмеження ресурсів: 100 од.
"Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од.
"Лимонного соку". Виробництво одиниці "Фруктового соку" вимагає 2 од.
"Фруктового пюре" та 1 од. "Води". Використовуючи PuLP, створіть модель, яка
визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити для
максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси.
Напишіть програму, код якої максимізує загальну кількість вироблених продуктів
"Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.

Статус розв'язку: Optimal Кількість виробленого Лимонаду: 30.0 Кількість
виробленого Фруктового соку: 20.0 Загальна кількість вироблених продуктів: 50.0

Завдання 2. Обчислення визначеного інтеграла.

Ваше друге завдання полягає в обчисленні значення інтеграла функції методом
Монте-Карло.

Порівняння результатів Оцінка інтегралу методом Монте-Карло:

Оцінка: приблизно 2.68608

Обчислення інтегралу за допомогою функції quad:

Інтеграл: 2.666666666666667

Оцінка абсолютної помилки: 2.960594732333751e-14

Висновки

Точність: Метод Монте-Карло надає наближену оцінку інтегралу, яка може
відрізнятися від точного значення, отриманого за допомогою аналітичних методів.
Результат, отриманий функцією quad, є значно точнішим.

Продуктивність: Метод Монте-Карло є корисним для оцінки інтегралів
багатовимірних функцій або коли інтеграл неможливо обчислити аналітично. Проте
для одномірних інтегралів, таких як у даному випадку, метод quad з SciPy є більш
ефективним та точним.

Порівняння: У даному прикладі метод Монте-Карло надав оцінку 2.68608, яка
близька до точного значення 2.666666666666667, але має більшу похибку. Функція
quad забезпечила точний результат з дуже малою абсолютною помилкою.
