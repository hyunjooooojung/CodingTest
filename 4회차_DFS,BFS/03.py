# 소수 찾기

# 문제 설명

# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.


from itertools import permutations

def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False
        return True
    
def solution(numbers):
    answer = 0                             # 소수의 갯수를 담는 변수
    number = [n for n in numbers]          # 입력받은 문자열을 리스트로 변환                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    for i in range(1, len(number)+1):      # 1부터 number의 개수만큼 모든 조합의 수를 구한다(순열 이용)
        ans = set(permutations(number, i))
        for a in ans:
            current_num = "".join(a)       # 문자열을 합친다.
            if current_num[0] == "0":      # 문자열의 시작이 0인 경우
                continue
            else:                          # current_num을 int로 변환해 소수인지 판별
                if is_prime_number(int(current_num)) == True:
                    answer += 1
    return answer
    