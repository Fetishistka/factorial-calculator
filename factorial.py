import math

def calculate_factorial(n):
    """
    Вычисляет факториал числа, используя библиотеку math для оптимизации
    
    Args:
        n (int): Положительное целое число
        
    Returns:
        int: Факториал числа n
        
    Raises:
        ValueError: Если введено отрицательное число
    """
    if not isinstance(n, int):
        raise TypeError("Требуется целое число")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    return math.factorial(n)

def main():
    while True:
        try:
            # Запрашиваем ввод у пользователя
            user_input = input("Введите положительное целое число для вычисления факториала (или 'q' для выхода): ")
            
            # Проверяем, хочет ли пользователь выйти
            if user_input.lower() == 'q':
                print("Программа завершена.")
                break
            
            # Преобразуем ввод в целое число и вычисляем факториал
            number = int(user_input)
            result = calculate_factorial(number)
            
            # Выводим результат
            print(f"Факториал числа {number} равен {result}")
            
        except ValueError as e:
            if str(e) == "Факториал отрицательного числа не определен":
                print("Ошибка: Введено отрицательное число. Пожалуйста, введите положительное целое число.")
            else:
                print("Ошибка: Введите корректное целое число.")
        except TypeError:
            print("Ошибка: Требуется ввести целое число.")
        except OverflowError:
            print("Ошибка: Результат слишком велик для вычисления.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()