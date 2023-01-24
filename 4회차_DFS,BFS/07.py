# 모음 사전

# 문제 설명

# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.


# 중복 순열 product 사용
from itertools import product

def solution(word):
    words = []                            
    for i in range(1, 6):                                      # word의 길이는 1이상 5이하 : range(1, 6)
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i): # 중복 순열 product 를 사용해서 단어를 조합하고
            words.append(''.join(list(j)))                     # 조합한 단어를 join으로 붙혀준다.

    words.sort()                                               # 만든 단어들을 오름차순으로 정렬해준다.
    return words.index(word) + 1                               # 몇 번째 단어인지 return (= index에서 1을 더해줘야한다.)


# 위 코드를 더 짧게 변경!
def solution(word):
    words = ["".join(list(j)) for i in range(1, 6) for j in product(["A", "E", "I", "O", "U"], repeat=i)]    
    words.sort()
    return words.index(word) + 1