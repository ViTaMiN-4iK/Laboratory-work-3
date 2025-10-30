"""Декоратор с параметрами в функциональном стиле."""

from functools import wraps
from datetime import datetime
import time


def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Декоратор с параметрами для повторения вызовов при ошибках.
    
    Args:
        max_attempts (int): Максимальное количество попыток
        delay (float): Задержка между попытками в секундах
        exceptions (tuple): Типы исключений для перехвата
        
    Returns:
        function: Декорированная функция с логикой повторения
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Попытка {attempt}/{max_attempts} для функции {func.__name__}")
                    result = func(*args, **kwargs)
                    
                    if attempt > 1:
                        print(f"✅ Успех на попытке {attempt}!")
                    
                    return result
                    
                except exceptions as e:
                    last_exception = e
                    print(f"❌ Ошибка на попытке {attempt}: {e}")
                    
                    if attempt < max_attempts:
                        print(f"⏳ Ожидание {delay} секунд перед следующей попыткой...")
                        time.sleep(delay)
            
            print(f"🚫 Все {max_attempts} попыток завершились ошибкой")
            raise last_exception
            
        return wrapper
    return decorator


def timer(unit="seconds"):
    """Декоратор с параметром для измерения времени выполнения.
    
    Args:
        unit (str): Единица измерения времени ('seconds', 'milliseconds')
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            execution_time = end_time - start_time
            
            if unit == "milliseconds":
                execution_time *= 1000
                time_str = f"{execution_time:.2f} мс"
            else:
                time_str = f"{execution_time:.6f} сек"
            
            print(f"⏱️ Функция {func.__name__} выполнилась за {time_str}")
            return result
            
        return wrapper
    return decorator


def validate_input(*validators):
    """Декоратор с параметрами для валидации входных данных.
    
    Args:
        *validators: Функции-валидаторы для аргументов
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"🔍 Валидация входных данных для {func.__name__}")
            
            # Валидация позиционных аргументов
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if validator:
                    validator(arg, f"аргумент {i}")
            
            # Валидация именованных аргументов
            for key, value in kwargs.items():
                print(f"   {key} = {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Функции-валидаторы
def validate_positive(value, param_name):
    """Валидатор положительных чисел."""
    if value <= 0:
        raise ValueError(f"{param_name} должен быть положительным числом")


def validate_integer(value, param_name):
    """Валидатор целых чисел."""
    if not isinstance(value, int):
        raise ValueError(f"{param_name} должен быть целым числом")


# Примеры использования декораторов с параметрами
@retry(max_attempts=3, delay=0.5, exceptions=(ValueError,))
@timer(unit="milliseconds")
def risky_division(a, b):
    """Рискованное деление с возможностью ошибки."""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b


@retry(max_attempts=2, delay=1)
@timer()
def simulate_network_request():
    """Имитация сетевого запроса с случайными ошибками."""
    import random
    
    if random.random() < 0.7:  # 70% вероятность ошибки
        raise ConnectionError("Сетевая ошибка")
    
    return "Данные получены успешно"


@validate_input(validate_positive, validate_positive)
@timer(unit="milliseconds")
def calculate_factorial(n):
    """Вычисление факториала с валидацией входных данных."""
    from functools import reduce
    from operator import mul
    
    return reduce(mul, range(1, n + 1), 1)


@retry(max_attempts=4, delay=0.2)
@validate_input(validate_integer, validate_positive)
def fibonacci_numbers(count):
    """Генерация чисел Фибоначчи."""
    from itertools import islice
    
    def fib_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    return list(islice(fib_generator(), count))


def main():
    """Демонстрация работы декораторов с параметрами."""
    print("=== ДЕКОРАТОРЫ С ПАРАМЕТРАМИ ===\n")
    
    # Тестирование декоратора retry
    print("1. Тестирование декоратора retry:")
    print("=" * 40)
    
    try:
        result = risky_division(10, 0)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Итоговая ошибка: {e}")
    
    print("\n" + "=" * 40)
    
    # Тестирование сетевого запроса
    print("\n2. Имитация сетевого запроса:")
    print("=" * 40)
    
    try:
        result = simulate_network_request()
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Итоговая ошибка: {e}")
    
    print("\n" + "=" * 40)
    
    # Тестирование валидации
    print("\n3. Тестирование валидации входных данных:")
    print("=" * 40)
    
    try:
        result = calculate_factorial(5)
        print(f"Факториал 5 = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 40)
    
    # Тестирование успешного сценария
    print("\n4. Успешный сценарий:")
    print("=" * 40)
    
    try:
        result = risky_division(10, 2)
        print(f"Результат деления: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 40)
    
    # Тестирование Фибоначчи
    print("\n5. Числа Фибоначчи:")
    print("=" * 40)
    
    try:
        result = fibonacci_numbers(8)
        print(f"Первые 8 чисел Фибоначчи: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()