
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    root = Node(heap[index])

    root.left = build_heap_tree(heap, 2 * index + 1)
    root.right = build_heap_tree(heap, 2 * index + 2)

    return root


# Обхід у глибину (DFS) за допомогою стека
def depth_first_search(root):
    if root is None:
        return []

    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        # Спочатку додаємо правого нащадка,
        # щоб лівий був оброблений першим
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return visited


# Обхід у ширину (BFS) за допомогою черги
def breadth_first_search(root):
    if root is None:
        return []

    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return visited


# Генерація кольорів від темного до світлого
def generate_colors(count):
    start_color = (10, 40, 80)       # Темно-синій
    end_color = (144, 224, 239)      # Світло-блакитний

    colors = []

    for i in range(count):
        if count == 1:
            ratio = 0
        else:
            ratio = i / (count - 1)

        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)

        colors.append(f"#{r:02X}{g:02X}{b:02X}")

    return colors


# Побудова графа та визначення позицій вузлів
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return

    graph.add_node(node.id, label=str(node.val))

    pos[node.id] = (x, y)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        add_edges(graph, node.left, pos, x - 1 / (2 ** layer), y - 1, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        add_edges(graph, node.right, pos, x + 1 / (2 ** layer), y - 1, layer + 1)


# Візуалізація дерева з кольорами обходу
def draw_tree(root, traversal, title):
    graph = nx.DiGraph()
    pos = {}

    add_edges(graph, root, pos)

    # Генеруємо кольори відповідно до порядку обходу
    colors = generate_colors(len(traversal))

    node_colors = {}
    node_labels = {}

    for index, node in enumerate(traversal):
        node_colors[node.id] = colors[index]
        node_labels[node.id] = f"{node.val}\n#{index + 1}"

    color_list = [
        node_colors[node_id]
        for node_id in graph.nodes()
    ]

    labels = {
        node_id: node_labels[node_id]
        for node_id in graph.nodes()
    }

    plt.figure(figsize=(10, 6))

    nx.draw(
        graph,
        pos,
        labels=labels,
        with_labels=True,
        node_color=color_list,
        node_size=2500,
        font_size=10,
        font_weight="bold",
        edge_color="gray",
        arrows=False
    )

    plt.title(title)
    plt.axis("off")
    plt.show()


# Створення бінарного дерева
heap = [0, 4, 1, 5, 10, 3]

root = build_heap_tree(heap)

# Обхід у глибину
dfs_result = depth_first_search(root)

# Обхід у ширину
bfs_result = breadth_first_search(root)

# Виведення порядку обходу
print("DFS (обхід у глибину):")
print([node.val for node in dfs_result])

print("\nBFS (обхід у ширину):")
print([node.val for node in bfs_result])

# Візуалізація результатів
draw_tree(root, dfs_result, "DFS - Depth-First Search")
draw_tree(root, bfs_result, "BFS - Breadth-First Search")
