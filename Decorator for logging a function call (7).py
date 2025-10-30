#Для решения задачи был использован ИИ-ассистент DeepSeek версии 3 (DeepSeek-V3) компании DeepSeek.

from functools import wraps
from datetime import datetime


def log_calls(level="INFO"):


    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем начало вызова
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{level}] {timestamp} - Вызов функции: {func.__name__}")
            
            # Логируем аргументы
            if args:
                print(f"[{level}] {timestamp} - Позиционные аргументы: {args}")
            if kwargs:
                print(f"[{level}] {timestamp} - Именованные аргументы: {kwargs}")
            
            # Выполняем функцию
            try:
                result = func(*args, **kwargs)
                
                # Логируем успешное завершение
                print(f"[{level}] {timestamp} - Функция {func.__name__} завершена успешно")
                print(f"[{level}] {timestamp} - Результат: {result}")
                
                return result
                
            except Exception as e:
                # Логируем ошибку
                print(f"[ERROR] {timestamp} - Ошибка в функции {func.__name__}: {e}")
                raise
        
        return wrapper
    return decorator


@log_calls(level="INFO")
def fibonacci_numbers(count):
    """Генерирует список чисел Фибоначчи."""
    from itertools import islice
    
    def fib_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    return list(islice(fib_generator(), count))


@log_calls(level="DEBUG")
def calculate_factorial(n):
    from functools import reduce
    from operator import mul
    
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    
    return reduce(mul, range(1, n + 1), 1)


@log_calls()
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def main():
    print("=== ДЕМОНСТРАЦИЯ ДЕКОРАТОРА ЛОГИРОВАНИЯ ===\n")
    
    # Тестирование различных функций
    functions_to_test = [
        lambda: fibonacci_numbers(5),
        lambda: calculate_factorial(5),
        lambda: greet("Анна", greeting="Привет"),
        lambda: greet("Мир")
    ]
    
    list(map(lambda func: func(), functions_to_test))
    
    print("\n" + "="*50)
    
    try:
        calculate_factorial(-1)
    except ValueError:
        print("Ошибка обработана корректно")


if __name__ == "__main__":
    main()