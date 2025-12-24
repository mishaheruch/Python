# Цикли for, while. Функція range(). Оператори break, continue, pass. Оператор else у циклі for.

## Теорія

### Мета: зрозуміти, чим відрізняються цикли for та while, а також побачити, де корисно застосовувати функцію range(). Зрозуміти, як break, continue та pass впливають на роботу циклу.

### 1. Прочитай і виконай приклад коду, який демонструє використання for: [ось він](https://docs.python.org/uk/3.13/tutorial/controlflow.html#for-statements).

### 2. Прочитай і виконай приклади коду, який демонструє використання while: [ось він](https://www.freecodecamp.org/ukrainian/news/tsykl-do-while-u-python-pryklad/).

### 3. Те саме для функції range(): [дивись тут](https://docs.python.org/uk/3.13/tutorial/controlflow.html#the-range-function).

### 4. Те саме для операторів [break та continue](https://docs.python.org/uk/3.13/tutorial/controlflow.html#break-and-continue-statements), [else у циклі for](https://docs.python.org/uk/3.13/tutorial/controlflow.html#else-clauses-on-loops) і оператора [pass](https://docs.python.org/uk/3.13/tutorial/controlflow.html#pass-statements).

## Завдання

У цій папці створи файл `sum.py` і напиши у ньому код, який буде приймати від користувача будь-яку кількість чисел, які розділені між собою пробілами. Мінімально чисел має бути 2. У відповідь функція має повертати суму усіх чисел, які увів користувач. Якщо неможливо визначити, які числа увів користувач, прорама має повернути повідомлення з помилкою.

Наприклад: якщо користувач введе `5 8 91`, то програма має повертати `104`. Або ж якшо користувач введе `-0.1 153 9.87 100.000006`, то програма має повертати `262.770006`.

_Підказка. Подумай, як можна створити список чисел із того, що увів користувач. Врахуй, що не усе, що він увів, може бути числом (наприклад, може бути таке: `91 test not_a_number 3 89 %^&$%^`). Використовуй цикли, щоб перевірити кожен елемент на число._

_Підказка 2. Для перевірки на float можна додати собі у файл таку функцію:_

```
def cast_to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0
```

_Потім її можна використовувати ось так:_

`float_value = cast_to_float(string_value)`


День. 03
range() дає йому числа, а for просто перебирає їх.
[5, 6, 7, 8, 9]
list(range(0, 10, 3))
старт → 0
крок → +3
зупинка перед 10
0 → 3 → 6 → 9
list(range(-10, -100, -30))
початок → -10
крок → -30 (рухаємось назад!)
зупинка перед -100
-10 → -40 → -70
for i, value in enumerate(a):
    print(i, value)
автоматично дає індекс
і елемент
без len() і без a[i]
number = 0
while number < 10:
    print(f"Числом є {number}!")
    number = number + 1
while означає:
“ПОВТОРЮЙ, ПОКИ умова істинна”
number = 0. Початкове значення змінної. 
while number < 10:  Цикл працює, поки number менше 10
number = number + 1
Без цього рядка цикл був би нескінченним ♾️
number = 0 → друк → +1
number = 1 → друк → +1
...
number = 9 → друк → +1
number = 10 → СТОП (умова false)
Числом є 0!
...
Числом є 9!
break = «далі не перевіряй, виходимо з циклу»
continue не зупиняє цикл, а просто переходить до наступної ітерації.
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
pass = “тут має бути код, але поки нічого”
