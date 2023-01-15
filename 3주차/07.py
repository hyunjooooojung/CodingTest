# 올바른 괄호

# 문제 설명

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

def solution(s):
    stack = []
    
    for i in s:
        if i == "(":          # 현재 괄호가 "("라면 stack에 현재괄호를 넣어준다.
            stack.append(i)
        else:
            if stack == []:   # stack이 빈 스택이면
                return False  # 올바르지 않은 괄호이기 때문에 False 
            else:             # stack이 비어있지 않으면
                stack.pop()   # 맨 끝에 있는 "("를 하나 pop
    
    if stack != []:           # stack이 빈 스택이 아니면
        return False          # 올바르지 않은 괄호이기 때문에 False
    return True

print(solution("()()"))  # True
print(solution(")("))    # False

# 1. "(" 를 저장할 괄호 스택 리스트를 선언.
# 2. 문자열 s에 있는 괄호들을 하나씩 반복.
# 3. 현재 괄호가 "("라면 stack에 현재괄호를 넣어준다.
# 4. 현재 괄호가 ")"라면 


# 다른 사람의 풀이
def solution2(s):
    return s.count('(') == s.count(')') and s.index('(') < s.index(')')

print(solution2("()()"))  # True
print(solution2(")("))    # False