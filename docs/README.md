
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

Math formulas

Area

Circle: S = πR²
Rectangle: S = ab
Square: S = a²
Triangle: S = sqrt(p * (p-a) * (p-b) * (p-c)) where p is semiperimeter
Perimeter

Circle: P = 2πR
Rectangle: P = 2a + 2b
Square: P = 4a
Triangle: P = a + b + c
Файл circle.py

Возвращает площадь и периметр круга.

1. Area.

def area(r):
    return math.pi * r * r
Принимает на вход радиус круга и возвращает его площадь.

Пример:

print(area(3))
Функция принимает значение 3 и возвращает площадь - 9π

2.Perimeter

def perimeter(r):
    return 2 * math.pi * r
Принимает на вход радиуc круга и возвращает его периметер.

Пример:

print(perimeter(3))
Функция принимает значение 3 и возвращает площадь - 6π

Файл square.py

Возвращает площадь и периметр квадрата.

1. Area.

def area(a):
    return a * a
Принимает на вход сторону квадрата и возвращает его площадь.

Пример:

print(area(3))
Функция принимает значение 3 и возвращает площадь - 9

2.Perimeter

def perimeter(a):
    return 4 * a
Принимает на вход сторону квадрата и возвращает его периметер.

Пример:

print(perimeter(3))
Функция принимает значение 3 и возвращает периметер - 12

Файл triangle.py

Возвращает площадь и периметр треугольника.

1. Area.

def area(a, b, c):
    return (a + b + c) / 2
Принимает на вход стороны треугольника и возвращает его площадь.

Пример:

print(area(3,4,5))
Функция принимает значение 3,4,5 и возвращает площадь - 6

2.Perimeter

def perimeter(a, b, c):
    return a + b + c
Принимает на вход стороны треугольника и возвращает его периметер.

Пример:

print(perimeter(3,4,5))
Функция принимает значение 3,4,5 и возвращает площадь - 12

История commits

ed65357 (HEAD -> documentation) add documentation to square.py
69a6d56 add documentation to triangle.py
93a4c7a add documentation to circle.py
9bbb8bb add documentation to calculate.py
b5b0fae (origin/develop, develop) L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added | * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info | * 438b89a L-05: Add user agreement | * 6adb962 L-03: Docs added | | * 3049431 (origin/feature) L-04: Add rectangle.py | |/ |/|
| d078c8d (origin/main, origin/HEAD, main) L-03: Docs added |/
8ba9aeb L-03: Circle and square added
