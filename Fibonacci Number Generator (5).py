#Для решения задачи был использован ИИ-ассистент DeepSeek версии 3 (DeepSeek-V3) компании DeepSeek.
from itertools import islice


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_numbers(count):
    return list(islice(fibonacci_generator(), count))


def main():
    try:
        n = int(input("Введите количество чисел Фибоначчи: "))
        
        if n <= 0:
            print("Пожалуйста, введите положительное число")
            return
            
        fib_numbers = get_fibonacci_numbers(n)
        print(f"Первые {n} чисел Фибоначчи: {fib_numbers}")
        
    except ValueError:
        print("Пожалуйста, введите целое число")


if __name__ == "__main__":
    main()