import heapq

def astar(graph, heuristic, start, goal):
    open_set = []

    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)

            return path[::-1]

        for neighbour, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + heuristic[neighbour]
                heapq.heappush(open_set, (f_score[neighbour], neighbour))
    return "No Path Found"

def main():
    graph = {}

    nodes = input("Enter nodes space separated: ").split()

    for node in nodes:
        neighbours = input(f"Enter node {node} neighbours (eg. A:4 B:5): ").split()
        graph[node] = {n.split(':')[0] : int(n.split(':')[1]) for n in neighbours}

    heuristic = {}
    print("Heuristic Values: ")
    for node in nodes:
        heuristic[node] = int(input(f"{node}: "))

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    path = astar(graph, heuristic, start, goal)
    print(f"Path from node {start} to node {goal} is {path}")

if __name__ == "__main__":
    main()
