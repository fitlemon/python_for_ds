import game_v2
import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Функция угадывания числа при помощи random с учетом информации о том, что случайное число больше или меньше загаданного

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    low, high = 1, 101
    while True:
        count += 1
        predict_number = np.random.randint(low, high)
        if predict_number > number:
            high = predict_number
        elif predict_number < number:
            low = predict_number + 1
        else:
            break
    return count


if __name__ == "__main__":
    # RUN
    game_v2.score_game(game_core_v3)
