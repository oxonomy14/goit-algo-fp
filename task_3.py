
import heapq


def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Створення мінімальної купи
    priority_queue = [(0, start)]

    while priority_queue:
        # Отримуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо застарілі значення
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідні вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Додаємо вершину з новою відстанню до купи
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Створюємо зважений граф
graph = {
    "A": {"B": 5, "D": 3},
    "B": {"A": 5, "C": 2, "E": 4},
    "C": {"B": 2, "F": 6},
    "D": {"A": 3},
    "E": {"B": 4},
    "F": {"C": 6}
}

# Знаходимо найкоротші шляхи від вершини A
start_vertex = "C"
result = dijkstra(graph, start_vertex)

# Виводимо результати
print(f"Найкоротші відстані від вершини {start_vertex}:")

for vertex, distance in result.items():
    print(f"До вершини {vertex}: {distance}")
