bfsGraph = {
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


def bfs(graph, start_node):
    visited = [] # 방문한 노드를 담을 배열
    queue = [] # 방문 예정인 노드를 담을 배열

    queue.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.

    while queue: # 더 이상 방문할 노드가 없을 때까지.
        node = queue.pop(0) # 방문할 노드를 앞에서 부터 하나씩 꺼내기.

        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            queue.extend(graph[node]) # 해당 노드의 자식 노드로 추가
    
    print("bfs - ", visited)
    return visited
    
    
# 함수 실행
bfs(bfsGraph, 'G')
# bfs -  ['G', 'D', 'C', 'E', 'B', 'F', 'A', 'H', 'I', 'J', 'M', 'K', 'L']