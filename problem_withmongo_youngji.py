from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.0.145:27017")    # mongodb 접속
database = mongoClient["toy_nosqls"]   # database 연결
# database[collection_name]        # collection 작업

collection_problem_list = database['problem_list']
collection_problem_answer = database['problem_answer']
collection_user = database['user']
collection_user_answer = database['user_answer']

# def insert_data():
#     problems = {
#             'question': '다음 중 파이썬에서 사용되는 산술 연산자가 아닌 것은?',
#             'answer': 4,
#             'score': 10
#         }
#         # {
#         #     'question': '파이썬에서 리스트의 길이를 확인하는 함수는?',
#         #     'answer': 1,
#         #     'score': 10
#         # }

#     answer = [
#             {'choices': '+'},
#             {'choices': '-'},
#             {'choices': '*'},
#             {'choices': '/'},
#             {'choices': '%'}
#             # {'choices': 'len()'},
#             # {'choices': 'size()'},
#             # {'choices': 'length()'},
#             # {'choices': 'sizeof()'},
#             # {'choices': 'count()'},
#     ]

#     problems_result = collection_problem_list.insert_one(problems)
#     problems_inserted_id = problems_result.inserted_id     #problem id

#     list_problems_answer = list()
#     for dict_answer in answer:
#         dict_answer["problems_id"] = problems_inserted_id
#         list_problems_answer.append(dict_answer)

#     collection_answer_list.insert_many(list_problems_answer)


def input_user_name():
    # 참여자 이름 입력
    user_name = input("응시자 이름을 입력하세요: ")
    user_id = collection_user.insert_one({"user_name" : user_name})
    inserted_user_id = user_id.inserted_id
    return inserted_user_id


def solving_problem():

    inserted_user_id = input_user_name()

    print("문제를 풀어주세요: ")

    doc = collection_problem_list.find({})
    num_count_question = 1

    for i in doc:
        # 문제 나열
        print(" 문항{}: {} / ".format(num_count_question, i["Question"]), end="")
        problem_id = i['_id']
        num_count_question+= 1
        doc2 = collection_problem_answer.find({"Question_id" : problem_id})

        # 답 나열
        print("선택지: ", end="")
        num_count_choices = 1
        for j in doc2:
            print("{}. {} ".format(num_count_choices, j["Answer"]), end="")
            num_count_choices += 1
        print("")

        # 답 입력
        user_answer = int(input(" 답: "))
        collection_user_answer.insert_one({"user_id" : inserted_user_id, "problem_id" : problem_id,"user_answer" : user_answer})

# 종료여부 묻기
def end():
    while True:
        user_end = input("다음 응시자가 있나요? (계속: c, 종료: x): ")
        if user_end == 'c':
            solving_problem()
        elif user_end == 'x':
            break
        else:
            print("c, x 중 하나를 입력해주세요.")


