def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")

choice = input("Введите номер операции (1/2/3): ")

if choice in ('1', '2', '3'):
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
else:
    print("Некорректный ввод операции.")