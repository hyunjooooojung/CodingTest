graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs_recursive(graph, node, visited=[]):
    visited.append(node)
    for near_node in graph[node]:
        if near_node not in visited:
            print(visited)
            dfs_recursive(graph, near_node, visited)
    return visited

dfs_recursive(graph, 'A')
'''
    ['A']
    ['A', 'B']
    ['A', 'B', 'H']
    ['A', 'B', 'H', 'I']
    ['A', 'B', 'H', 'I', 'J']
    ['A', 'B', 'H', 'I', 'J', 'K']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E', 'F']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E', 'F', 'G']
'''


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph_a = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_recursion(graph_a, start_node, visited=[]):
    visited.append(start_node)
    for node in graph_a:
        if node not in visited:
            dfs_recursion(graph_a, node, visited)
    
    return visited


print(dfs_recursion(graph_a, 1)) # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
