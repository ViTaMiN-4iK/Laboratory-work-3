#Для решения задачи был использован ИИ-ассистент DeepSeek версии 3 (DeepSeek-V3) компании DeepSeek.


def calculate_squares():
    numbers = range(1, 11)
    
    # Используем map с лямбда-функцией
    squares = list(map(lambda x: x ** 2, numbers))
    
    return squares


def calculate_squares_with_details():
    numbers = list(range(1, 11))
    
    # Функциональный подход: map + лямбда
    squares = list(map(lambda x: x ** 2, numbers))
    
    # Создаем список кортежей (число, квадрат) с помощью zip и map
    results = list(zip(numbers, squares))
    
    return results


def format_output(results):
    return list(map(lambda pair: f"{pair[0]}² = {pair[1]}", results))


def main():
    print("=== ВЫЧИСЛЕНИЕ КВАДРАТОВ ЧИСЕЛ 1-10 С MAP ===\n")
    
    # Простой вариант
    squares = calculate_squares()
    print("Квадраты чисел 1-10:")
    print(squares)
    
    print("\n" + "=" * 40 + "\n")
    
    # Детализированный вариант
    detailed_results = calculate_squares_with_details()
    formatted_output = format_output(detailed_results)
    
    print("Детализированные результаты:")
    for item in formatted_output:
        print(item)
    
    print("\n" + "=" * 40 + "\n")
    
    # Чисто функциональный подход в одну строку
    print("Функциональный подход в одну строку:")
    final_result = list(
        map(
            lambda pair: f"{pair[0]}² = {pair[1]}", 
            zip(range(1, 11), map(lambda x: x ** 2, range(1, 11)))
        )
    )
    
    for item in final_result:
        print(item)


if __name__ == "__main__":
    main()