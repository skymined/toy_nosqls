from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.0.145:27017")    # mongodb 접속
# mongoClient = MongoClient("mongodb://192.168.0.65:27017")    # mongodb 접속
database = mongoClient["toy_nosqls"]   # database 연결

collection_problem_list = database['problem_list']
collection_problem_answer = database['problem_answer']
collection_user = database['user']
collection_user_answer = database['user_answer']

Question = [
{
    'Question': '다음 중 파이썬에서 사용되는 산술 연산자가 아닌 것은?',
    'Answer': ['+', '-', '*', '/', '%'],
    'answer': 4,  # '/' is the fourth choice
    'score': 10
},
{
    'Question': '파이썬에서 리스트의 길이를 확인하는 함수는?',
    'Answer': ['len()', 'size()', 'length()', 'sizeof()', 'count()'],
    'answer': 1,  # 'len()' is the first choice
    'score': 10
}]

# data 입력
def insert_data():
    collection_problem_list.delete_many({})
    collection_problem_answer.delete_many({})

    problems_result = collection_problem_list.insert_many(Question)
    problems_inserted_ids = problems_result.inserted_ids

    for i, problem_id in enumerate(problems_inserted_ids):
        list_problems_answer = [{'Answer': choice, 'Question_id': problem_id} for choice in Question[i]['Answer']]
        collection_problem_answer.insert_many(list_problems_answer)
        collection_problem_list.update_many({}, {'$unset': {'Answer': ""}})


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

# insert_data()
# solving_problem()
# end()