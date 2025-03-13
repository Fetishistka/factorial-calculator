import math

def calculate_factorial(n):
    """
    Вычисляет факториал числа n, используя библиотеку math для оптимизации.
    Args:
        n (int): Положительное целое число
    Returns:
        int: Факториал числа n
    """
    return math.factorial(n)

def main():
    print("Добро пожаловать в программу вычисления факториала!")
    print("Пожалуйста, введите положительное целое число.")
    
    while True:
        try:
            # Запрашиваем ввод у пользователя
            user_input = input("Введите число (или 'q' для выхода): ")
            
            # Проверка на выход из программы
            if user_input.lower() == 'q':
                print("До свидания!")
                break
            
            # Преобразуем ввод в целое число
            number = int(user_input)
            
            # Проверяем, что число положительное
            if number < 0:
                print("Ошибка: Число должно быть положительным!")
                continue
            
            # Вычисляем факториал
            result = calculate_factorial(number)
            
            # Выводим результат
            print(f"Факториал числа {number} равен: {result}")
            
        except ValueError as ve:
            # Обработка нечислового ввода
            if "invalid literal" in str(ve):
                print("Ошибка: Пожалуйста, введите целое число!")
            else:
                print(f"Произошла ошибка: {ve}")
                
        except OverflowError:
            # Обработка слишком большого числа
            print("Ошибка: Число слишком большое для вычисления!")
            
        except Exception as e:
            # Обработка других возможных ошибок
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()