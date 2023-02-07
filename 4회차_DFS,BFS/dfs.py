dfsGraph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
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

def dfs(graph, start_node):
    visited = [] # 방문한 노드를 담을 배열
    stack = [] # 정점과 인접한 방문 예정인 노드를 담을 배열

    stack.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.

    while stack: # 더 이상 방문할 노드가 없을 때까지.
        node = stack.pop() # 방문할 노드를 앞에서 부터 하나씩 꺼내기.

        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            # stack.extend(graph[node]) # 해당 노드의 자식 노드로 추가
            stack.extend(reversed(graph[node]))

    print("dfs - ", visited)
    return visited
    
# 함수 실행
dfs(dfsGraph, 'G')
# dfs -  ['G', 'D', 'C', 'B', 'A', 'H', 'I', 'J', 'K', 'L', 'M', 'E', 'F']


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
adjacent_graph = {
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


def dfs_stack(adjacent_graph, start_node):
    # 구현해보세요!
    visited = []
    stack = [start_node]
  
    while stack: # 스택이 비어있지 않으면
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
        
    return visited


print(dfs_stack(adjacent_graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!