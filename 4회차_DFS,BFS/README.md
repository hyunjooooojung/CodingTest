<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Programmers&fontSize=90" />
</div>

# ⏳ 완전탐색 ⏳

## DFS (Depth-First Search)
- '깊이우선탐색(DFS)'은 가장 깊은 노드까지 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동하여 탐색을 합니다.
- root 노드(혹은 다른 임의의 노드)에서 시작하여 다른 branch로 넘어가기 전에 해당 branch를 전부 탐색하는 방식을 말합니다.

 
### 🤔 어떨 때 사용하는가?
주로 모든 노드를 방문하고자 하는 경우에 사용됩니다.

- 미로 찾기
- 그래프의 위상 정렬
- 모든 경우 다 해보기(전체 탐색)
- 연결 구성 요소 찾기
- 이분 그래프


### 🤔 어떻게 구현?
stack 또는 재귀함수를 사용하여 구현합니다.


### 🔍 예제코드 풀이
    1. 시작 정점을 먼저 stack[0]에 넣어줍니다.
    2. 그리고 스택에서 가장 위(top)에 있는 원소를 하나 꺼냅니다.
    3. 그 원소를 방문표시(visited)하고, 그 원소와 인접한 정점들 중에서 방문하지 않은 정점들을 모두 스택에 넣습니다.
    4. 방문의 우선순위에 따라 인접한 정점이 여러 개면 번호(알파벳이)가 작은 순서대로 방문해야 하므로, 순서에 맞게 스택에 넣어줍니다.
    5. 계속해서 스택의 가장 위에 있는 원소를 꺼내 방문표시하고, 해당 원소와 인접한 원소 중 방문하지 않은 원소들을 모두 스택에 넣어주는 과정을 반복합니다.


<br>


## BFS (Breath-First Search)
- '너비우선탐색(BFS)'는 root노드에서 인접한 노드를 먼저 탐색하는 방법입니다.
- 시작 정점으로부터 가장 가까운 정점을 먼저 방문하고, 멀리 떨어져 있는 정점은 나중에 방문하는 식으로 탐색하는 방식을 말합니다.

 
### 🤔 어떨 때 사용하는가?
주로 최단 경로 문제에서 사용됩니다.

- 두 정점 u,v 간의 최단 경로 찾기( 경로의 길이는 간선의 수에 따라 정해질 때)
- 문자열 알고리즘 Aho-Corasick 패턴 매칭(순위다중패턴매칭)의 실패함수를 구축할 때
- 그래프에서 정점들이 두 개의 독립적인 서로소 그룹으로 나누어질 수 있는가에 대해 이분성 테스트를 할 때
- copying garbage collection
- cheney's algorithm


### 🤔 어떻게 구현?
queue를 사용하여 구현합니다.


### 🔍 예제코드 풀이
    1. 시작 정점을 먼저 queue[0]에 추가해 줍니다.
    2. queue에서 제일 앞에 있는 원소를 하나 꺼냅니다.(pop)
    3. 그 원소를 방문표시(visited)하고, 그 원소와 인접한 정점들 중 방문완료되지 않았고, queue에 추가되지 않은 인접한 원소들을 queue에 추가해줍니다.
    4. queue가 빌 때까지 반복합니다.


<br>


참고자료 : https://nareunhagae.tistory.com/17

<br>
<hr>
<br>


## 프로그래머스 완전탐색 문제풀이

### 1. 최소직사각형([https://school.programmers.co.kr/learn/courses/30/lessons/86491](https://school.programmers.co.kr/learn/courses/30/lessons/86491))
### 풀이
    1. 명함 지갑의 가로, 세로 길이 후보 list 변수 w, h 생성한다
    2. 주어진 명함들을 for 문을 돌면서 더 큰 값을 w, 작은 값을 h에 저장한다
    3. 각 w, h 리스트에서 가장 큰 값을 곱한다
    
<br>

### 2. 모의고사([https://school.programmers.co.kr/learn/courses/30/lessons/42840](https://school.programmers.co.kr/learn/courses/30/lessons/42840))
    1. number1 : 1번 수포자 / number2 : 2번 수포자 / number3 : 3번 수포자
    2. score : 수포자 1,2,3의 점수를 담은 배열
    3. 정답이 담긴 배열 answers를 반복
    4. 현재 문제의 정답과 1번 수포자가 찍은 답이 일치한다면
    5. 1번 수포자의 점수에 1을 더한다.
    6. 현재 문제의 정답과 2번 수포자가 찍은 답이 일치한다면
    7. 2번 수포자의 점수에 1을 더한다.
    8. 현재 문제의 정답과 3번 수포자가 찍은 답이 일치한다면
    9. 3번 수포자의 점수에 1을 더한다.
    10. 점수가 담긴 배열 score안에서 반복
    11. 현재 수포자의 점수와 가장 높은 점수가 같으면
     
<br>


### 3. 소수찾기([https://school.programmers.co.kr/learn/courses/30/lessons/42839](https://school.programmers.co.kr/learn/courses/30/lessons/42839))
    1. is_prime_number -> 소수찾기 함수 
    2. answer: 소수의 갯수를 담는 변수 / number : 입력받은 문자열을 리스트로 변환                                                                                         3. 1부터 number의 개수만큼 모든 조합의 수를 구한다(순열 이용)
    4. current_num : 문자열을 합친다.
    5. current_num의 시작이 0인 경우
    6. current_num을 int로 변환해 소수인지 판별
    
<br>


### 4. 카펫 ([https://school.programmers.co.kr/learn/courses/30/lessons/42842](https://school.programmers.co.kr/learn/courses/30/lessons/42842))
    1. 전체 격자 개수 total
    2. 가로 or 세로 : i or j / yellow가 1 이상이려면 가로의 길이는 3이상이어야 함.
    3. 전체 격자 개수를 i로 나눴을 때 나누어 떨어지면 = 약수이면
    4. i * j == total 이니까 j = total // i
    5. 가로 길이가 세로길이보다 같거나 길기 때문에 내림차순 정렬!
    
<br>


### 5. 피로도([https://school.programmers.co.kr/learn/courses/30/lessons/87946](https://school.programmers.co.kr/learn/courses/30/lessons/87946))
    1. 순열을 이용해서 하루에 탐험할 수 있는 던전의 경우의 수를 모두 구한 후 그 안에서 반복
    2. 던전의 경우의 수 안에서 피로도 계산 (a = 최소 필요 피로도, b = 소모 피로도)
    3. 현재 피로도와 최소 필요 피로도, 소모 피로도 비교해서 최댓값 구하기
    
<br>

### 6. 전력망을 둘로 나누기([https://school.programmers.co.kr/learn/courses/30/lessons/86971](https://school.programmers.co.kr/learn/courses/30/lessons/86971))
    1. 
    2. 
    3. 
    
<br>


### 7. 모음사전([https://school.programmers.co.kr/learn/courses/30/lessons/84512](https://school.programmers.co.kr/learn/courses/30/lessons/84512))
    1. word의 길이는 1이상 5이하 : range(1, 6)
    2. 중복 순열 product 를 사용해서 단어를 조합하고, 조합한 단어를 join으로 붙혀준다.
    3. 만든 단어들을 오름차순으로 정렬해준다.
    4. index +1 return
