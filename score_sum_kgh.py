# —--------------------------------------------------
# 각 문항 정답  (예: 1, 2, 3, 4, 1): 1, 2, 3, 4, 1


# 응시자별 채점 결과:
#   홍길동: 95점
#   이순신: 85점
#   ...
# 과목 평균 점수: 90점


list_questions = ["question: 다음 중 파이썬에서 사용되는 산술 연산자가 아닌 것은?",
                "question: 파이썬에서 리스트의 길이를 확인하는 함수는?",
                 "question: 파이썬에서 문자열을 분할하는 함수는?",
                 "question: 파이썬에서 불변의 순서가 있는 자료형은?"]

list_choices = ["choices: 1. +, 2. -, 3. *, 4. /,5. %]",
                "choices: 1. len(), 2. size(), 3. length(), 4. sizeof(), 5. count()",
                "choices: 1. split(), 2. divide(), 3. slice(), 4. cut(), 5. part()",
                "choices: 1. List, 2. Dictionary, 3. Set, 4. Tuple, 5. None"]

list_statistics = [0,0,0,0]
for i in range(len(list_questions)) :
    print("{}. {}".format(i +1, list_questions[i]))
    print("{}".format(list_choices[i]))

    print("")
    num_answer = int(input("정답 : "))
    index = num_answer - 1
    list_statistics[index] = list_statistics[index] + 1

print("-----------------------------")
print("각 문항 정답 : {}".format(list_statistics))


