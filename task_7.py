"""
Завдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
"""

import random
from collections import Counter
import matplotlib.pyplot as plt


def monte_carlo_dice(num_rolls=100_000):
    # Можливі суми двох кубиків
    sums = range(2, 13)

    # Лічильник для кожної можливої суми
    counts = Counter()

    # Симуляція кидків двох кубиків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2
        counts[total] += 1

    # Теоретичні кількості комбінацій для кожної суми
    combinations = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    }

    # Обчислення ймовірностей
    probabilities = {total: counts[total] / num_rolls for total in sums}

    theoretical = {total: combinations[total] / 36 for total in sums}

    # Виведення таблиці результатів
    print(f"Кількість кидків: {num_rolls}\n")
    print(
        f"{'Сума':<8}" f"{'Кількість':<14}" f"{'Монте-Карло':<18}" f"{'Теоретична':<15}"
    )
    print("-" * 55)

    for total in sums:
        print(
            f"{total:<8}"
            f"{counts[total]:<14}"
            f"{probabilities[total]:<18.4%}"
            f"{theoretical[total]:<15.4%}"
        )

    # Побудова графіка
    x = list(sums)
    monte_carlo_values = [probabilities[total] for total in sums]
    theoretical_values = [theoretical[total] for total in sums]

    plt.figure(figsize=(10, 6))

    plt.bar(
        x,
        monte_carlo_values,
        width=0.6,
        label="Метод Монте-Карло",
    )

    plt.plot(
        x,
        theoretical_values,
        marker="o",
        linestyle="--",
        label="Теоретична ймовірність",
    )

    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xlabel("Сума чисел на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.xticks(x)
    plt.grid(axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    monte_carlo_dice()
