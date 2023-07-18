def is_prime(n):
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return "Число составное"
    return "Число простое"


number = int(input("Введите целое число от 1 до 100000: "))
if 0 < number <= 100000:
    print(is_prime(number))
else:
    print("Введите число в диапазоне от 1 до 100000")

