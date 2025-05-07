

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    result = []

    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            result.append(current)

            if current == goal:
                return result

            for neighbour in reversed(graph[current]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return "No Path Found"

        

            
    

def main():
    graph = {}

    n = int(input("Enter no .of edges: "))
    for i in range(n):
        u, v = input(f"Enter vertex pair for edge {i+1}: ").split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    path = dfs(graph, start, goal)
    print(f"Path from  node {start} to node {goal} is {path}")

if __name__ == "__main__":
    main()
