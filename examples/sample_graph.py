from levit import levit
# Пример графа (направленный, с положительными рёбрами)
graph = [
    [(1, 2), (2, 4)],        # 0
    [(2, 1), (3, 7)],        # 1
    [(4, 3)],                # 2
    [(5, 1)],                # 3
    [(3, 2), (5, 5)],        # 4
    []                       # 5
]

distances = levit(graph, start=0)
print("Кратчайшие расстояния от вершины 0:")
for i, d in enumerate(distances):
    print(f"До вершины {i}: {d}")
