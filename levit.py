from collections import deque

def levit(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    state = [0] * n  # 0 — M0, 1 — M1, 2 — M2
    dist[start] = 0
    queue = deque([start])
    state[start] = 1

    while queue:
        u = queue.popleft()
        state[u] = 2
        for v, w in graph[u]:
            if state[v] == 0 or dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if state[v] == 2:
                    queue.appendleft(v)
                elif state[v] == 0:
                    queue.append(v)
                state[v] = 1

    return dist
