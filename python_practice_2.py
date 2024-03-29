# -*- coding: utf-8 -*-
"""python_practice_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zOSSBMn9iZUF1uDLyv8ZzWMMZrnPlZGt

# I. Змінні та памʼять.

1. Створити змінні, що посилаються на два цілих числа, що однакові за значенням, де значення належить проміжку від -5 до 256. Перевірте, чи будуть ці змінні рівні тільки за значенням або ж ще будуть посилатися на один і той самий обʼєкт в памʼяті? Наведіть код та дайте текстову відповідь нижче.
"""

a = 5
b = 5

print(a == b)
print(id(a))
print(id(b))

"""У Python цілі числа від -5 до 256 зберігаються в пулі маленьких цілих чисел, тому коли створюються дві змінні з однаковим значенням в цьому діапазоні, обидві змінні посилаються на один і той же об'єкт в пам'яті.

2. За допомогою якої функції можна перевірити належність змінної до вказаного типу даних (напр. чи змінна True посилається на значення булевого та цілочисленого типу)?
"""

a = True
print(isinstance(a, bool))
print(isinstance(a, int))

"""# II. Цілі числа та числа з рухомою комою

3. Створити дві змінні, що посилаються на будь-які ціле число та число з рухомою комою та продемонструвати такі арифметичні операції: додавання, віднімання, ділення, множення, ділення без залишку, ділення по модулю, приведення до ступеню. Всі результати операцій вивести на екран.
"""

a = 5
b = 2.5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

"""4. Використовуючи змінні з вправи 3, продемонструйте механізм явного перетворення типів, де числа з рухомою комою перетворюються на цілі числа. Також визначте змінну, що посилається на значення булевого типу і спробуйте явно привести її до цілого числа."""

print(int(b))

c = True
print(int(c))

"""# IІІ. Рядки (String).

5. Створити пустий рядок двома різними способами.
"""

empty = ''
empty_1 = ""

"""6. Створити рядок з апострофом. Зробити його сирим. Вивести обидва рядка на екран."""

a = "I'm good, thanks"
b = r"I'm good, thanks"
print(a)
print(b)

"""7. Створити змінну, що буде посилатися на Ваше прізвище латинкою. Створити форматований рядок, який буде мати вигляд "My surname is ______", де на місці нижніх підкреслень буде Ваше прізвище зі змінної."""

surname = 'Kuryleno'
sentense = f'My surname is {surname}'
print(sentense)

"""8. Маючи рядок "My dog is crazy." перетворити його на список ["my", "dog", "is", "crazy"]"""

s = "My dog is crazy."
words_list = s.lower().strip('.').split()
print(words_list)

"""# IV. Робота зі списками.

9. Створити список двома різними за синтаксисом способами. За допомогою вбудованої функції обчисліть довжину одного з них.
"""

first_list = []
second_list = list()
print(len(first_list))

"""10. Створіть два списка та за допомогою спеціального методу додайте другий з них в якості останнього елемента першого."""

second_list = list((1, 2, 3))
third_list = list((4,))
second_list.append(third_list)
print(second_list )

"""11. Створіть список, де елементами цього списку також є списки. Отримай перший елемент з останнього рядка та виведи значення на екран."""

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[-1][0])

"""12. Створіть список з десяти елементів різного типу. Отримайте всі елементи, окрім двох перших та двох останніх та збережіть їх в новій змінній."""

a = [1, 2, True, None, 'house', ['trip'], (3, 4), 5.777, 'roar', False]
b = a[2:8]
print(b)

"""# V. Робота з кортежами.

14. Створити кортеж з один елементом.
"""

a = (1, )
print(isinstance(a, tuple))

"""15. Порівняйте список та кортеж. Назвіть схожості та відмінності, випадки використання.

Схожості

Індексація та зрізи: Обидва типи підтримують індексацію та зрізи для доступу та управління елементами.
Можуть зберігати різні типи даних: Як списки, так і кортежі можуть зберігати елементи різних типів даних.
Вкладеність: Обидва можуть містити інші списки або кортежі, створюючи вкладені структури даних.

Відмінності

Змінюваність: Списки є змінюваними (mutable), тобто їх вміст можна змінювати після створення. Кортежі є незмінними (immutable), тобто після створення їх вміст змінити не можна.
Використання пам'яті: Кортежі ефективніші за списки з точки зору використання пам'яті через їх незмінність.
Продуктивність: Операції з кортежами, загалом, виконуються швидше, ніж зі списками, через ту саму незмінність.
Методи: Списки мають більше вбудованих методів для маніпулювання даними (наприклад, append(), remove(), pop()), в той час як кортежі мають обмежену кількість методів.

Випадки використання

Списки: Ідеально підходять для колекцій, які можуть змінюватися протягом часу, наприклад, списки покупок, елементи в програмі, що потребують додавання, видалення або зміни.
Кортежі: Використовуються, коли необхідно гарантувати незмінність даних, наприклад, в якості ключів словника або коли потрібно оптимізувати використання пам'яті та продуктивність.

16. Створіть кортеж з 11ти елементів чисел з рухомою комою та отримайте кожен парний за індексом елемент в зворотньому порядку. Наприклад, маючи (1.2, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 0.3), отримати (0.3, 8.3, 6.3, 4.3, 2.3). Результат збережіть в нову змінну та виведіть на екран.
"""

a = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1, 11.2)
b = a[-2::-2]
print(b)

"""# VI. Множини (Set).

17. Створити множину без елементів. Після цого за допомогою методу додайте кілька різних елементів до множини. Чи множини є змінним типом даних?
"""

set_var = set(())
dir(set_var)
set_var.update([1, 2])
print(set_var)

"""Так, множини є змінним типом даних. Це означає, що після їх створення ви можете змінювати їх вміст, додаючи або видаляючи елементи.

18. Створити множину, маючи список my_list = [1, 1, 2, 67, 67, 8, 9]. Пояснити, чому "зникли" деякі елементи.
"""

first_set = {1, 1, 2, 67, 67, 8, 9}
print(first_set)

"""Коли список перетворюється на множину, "зникають" деякі елементи через унікальність, яка є основною характеристикою множини в Python. Множина — це невпорядкована колекція елементів, де кожен елемент є унікальним. Якщо в ітерованому об'єкті, з якого створюється множина, є дублікати, вони будуть автоматично видалені в процесі створення множини, залишивши кожен елемент унікальним.

19. Створіть дві множини. Продемонстуйте над ними операції: обʼєднання, різниці, пересічі та симетричної різниці. Використовуйте методи, що не змінюють множини, а створюють нові.
"""

a = {1, 2, 3}
b = {1, 4, 5}

union = a.union(b)
print(f"Об'єднання: {union}")

difference_a_b = a.difference(b)
print(f"Різниця a - b: {difference_a_b}")

intersection = a.intersection(b)
print(f"Пересічення: {intersection}")

symmetric_difference = a.symmetric_difference(b)
print(f"Симетрична різниця: {symmetric_difference}")

"""# VII. Словники (Dictionary).

20. Створіть пустий словник. До нього додайте чотири пари елементів такі, щоб їхні ключі були різних типів. Чи може список бути ключем? Чому?
"""

my_dict = {}

my_dict[1] = "integer"
my_dict["string"] = "string"
my_dict[3.14] = "float"
my_dict[(5, 7)] = "tuple"

print(my_dict)

"""Список не може бути ключем у словнику в Python через його змінну природу. Ключі в словнику повинні бути об'єктами не змінного типу

21. Створіть словник, де значенням в одній з пар теж буде словник, який теж має вкладений словник. Виведіть на екран значення, що міститься в словнику, що знаходиться на найнижчому рівні ієрархії вкладеності (найбільш внутрішній).
"""

dictionary = {"level_1": {"level_2": {"level_3": "Innermost value"}}}
value = dictionary["level_1"]["level_2"]["level_3"]
print(value)

"""# Вітаю! Ви велика(ий) молодець, що впоралась(вся). Похваліть себе та побалуйте чимось приємним. Я Вами пишаюся."""