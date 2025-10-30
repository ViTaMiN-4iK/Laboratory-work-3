#Для решения задачи был использован ИИ-ассистент DeepSeek версии 3 (DeepSeek-V3) компании DeepSeek.

import csv
import os
from typing import List, Dict, Any


def create_sample_csv():
    if not os.path.exists('users.csv'):
        data = [
            ['name', 'age', 'city', 'salary'],
            ['Иван', '30', 'Москва', '60000'],
            ['Мария', '25', 'Санкт-Петербург', '45000'],
            ['Петр', '35', 'Казань', '75000'],
            ['Анна', '22', 'Новосибирск', '35000'],
            ['Сергей', '28', 'Екатеринбург', '52000'],
            ['Ольга', '40', 'Владивосток', '48000']
        ]
        
        with open('users.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("✅ Создан пример файла users.csv")


def read_csv_file(filename: str) -> List[Dict[str, Any]]:
    """Читает CSV файл и возвращает список словарей."""
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def filter_and_transform_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует и преобразует данные используя map/filter."""
    
    # Фильтрация: оставляем только пользователей старше 25 лет
    filtered_data = list(filter(lambda row: int(row['age']) > 25, data))
    
    # Преобразование
    transformed_data = list(map(lambda row: {
        'name': row['name'].upper(),
        'age': int(row['age']),
        'city': row['city'].title(),
        'salary': float(row['salary']),
        'salary_category': 'HIGH' if float(row['salary']) > 50000 else 'LOW'
    }, filtered_data))
    
    return transformed_data


def run_tests():
    """Запускает тесты для функций обработки данных."""
    print("🧪 Запуск тестов...")
    
    try:
        # Создаем тестовый файл если его нет
        create_sample_csv()
        
        # Читаем данные из файла для тестов
        test_data = read_csv_file('users.csv')
        
        # Тест 1: Проверяем что файл читается корректно
        assert len(test_data) > 0, "Файл пустой или не читается"
        print("✅ Тест чтения файла пройден")
        
        # Тест 2: Фильтрация по возрасту
        result = filter_and_transform_data(test_data)
        expected_count = len([row for row in test_data if int(row['age']) > 25])
        assert len(result) == expected_count, f"Тест фильтрации: ожидалось {expected_count}, получено {len(result)}"
        print("✅ Тест фильтрации по возрасту пройден")
        
        # Тест 3: Преобразование данных
        if len(result) > 0:
            assert result[0]['name'].isupper(), "Имя должно быть в верхнем регистре"
            assert isinstance(result[0]['age'], int), "Возраст должен быть int"
            assert isinstance(result[0]['salary'], float), "Зарплата должна быть float"
            print("✅ Тест преобразования данных пройден")
        
        print("🎉 Все тесты успешно пройдены!")
        return True
        
    except Exception as e:
        print(f"❌ Тест провален: {e}")
        return False


def main():
    # Запускаем тесты
    tests_passed = run_tests()
    print()
    
    if not tests_passed:
        print("⚠️  Тесты не пройдены, выполнение основной логики прервано")
        return
    
    try:
        # Чтение и обработка данных
        original_data = read_csv_file('users.csv')
        processed_data = filter_and_transform_data(original_data)
        
        # Вывод результатов
        print("📋 Обработанные данные:")
        for row in processed_data:
            print(f"{row['name']} | {row['age']} | {row['city']} | {row['salary']} | {row['salary_category']}")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    main()