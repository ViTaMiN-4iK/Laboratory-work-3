#Для решения задачи был использован ИИ-ассистент DeepSeek версии 3 (DeepSeek-V3) компании DeepSeek.

from functools import wraps
import time


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        print(f"✅ Успех на попытке {attempt}!")
                    return result
                except Exception as e:
                    print(f"❌ Попытка {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise Exception(f"Все {max_attempts} попыток завершились ошибкой")
        return wrapper
    return decorator


def timer(unit="seconds"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            execution_time = end_time - start_time
            if unit == "milliseconds":
                execution_time *= 1000
                print(f"⏱️ Время выполнения: {execution_time:.2f} мс")
            else:
                print(f"⏱️ Время выполнения: {execution_time:.6f} сек")
                
            return result
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
@timer(unit="milliseconds")
def risky_operation(x, y):
    if y == 0:
        raise ValueError("Деление на ноль!")
    return x / y


@retry(max_attempts=2, delay=1)
def network_call():
    import random
    if random.random() < 0.6:
        raise ConnectionError("Сбой соединения")
    return "Данные получены"


def main():
    print("=== ДЕКОРАТОРЫ С ПАРАМЕТРАМИ ===\n")
    
    # Тест 1: Деление с ошибкой
    print("1. Тест деления:")
    try:
        result = risky_operation(10, 0)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 30)
    
    # Тест 2: Успешное деление
    print("2. Успешное деление:")
    try:
        result = risky_operation(10, 2)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n" + "=" * 30)
    
    # Тест 3: Сетевой вызов
    print("3. Сетевой вызов:")
    try:
        result = network_call()
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()