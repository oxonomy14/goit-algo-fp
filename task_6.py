items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    # Отримуємо список страв
    food_items = list(items.items())
    n = len(food_items)

    # Створюємо таблицю для збереження результатів
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю динамічного програмування
    for i in range(1, n + 1):
        name, data = food_items[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for b in range(budget + 1):
            # Не беремо поточну страву
            dp[i][b] = dp[i - 1][b]

            # Беремо страву, якщо вистачає бюджету
            if cost <= b:
                dp[i][b] = max(
                    dp[i][b],
                    dp[i - 1][b - cost] + calories
                )

    # Відновлюємо оптимальний набір страв
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, data = food_items[i - 1]
            selected_items.append(name)
            b -= data["cost"]

    selected_items.reverse()

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in selected_items)

    return selected_items, total_calories, total_cost


# Встановлюємо бюджет
budget = 100

# Виконуємо жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)

# Виконуємо алгоритм динамічного програмування
dp_result = dynamic_programming(items, budget)


print(f"Бюджет: {budget}")
print("\nЖадібний алгоритм:")
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Загальна вартість: {greedy_result[2]}")
print(f"Загальна калорійність: {greedy_result[1]}")

print("\nДинамічне програмування:")
print(f"Вибрані страви: {dp_result[0]}")
print(f"Загальна вартість: {dp_result[2]}")
print(f"Загальна калорійність: {dp_result[1]}")