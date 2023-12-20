from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.0.145:27017")    # mongodb 접속
database = mongoClient["toy_nosqls"]   # database 연결

# 각 collection에 대해 변수 선언
coll_problem_list = database['problem_list']
coll_problem_answer = database['problem_answer']
coll_user = database['user']
coll_user_answer = database['user_answer']

# 각 collection find하여 변수 선언
problem = list(coll_problem_list.find({}))
problem_answer = list(coll_problem_answer.find({}))
user = list(coll_user.find({}))
user_answer = list(coll_user_answer.find({}))

# 각 문항 정답 출력에 대한 구문
def answer_data(problem):
    print("-------------------")
    print("각 문항 정답 : ", end="")
    problems = list(str(num['correct_answer']) for num in problem)  # 'correct_answer' 값들을 리스트에 저장
    print(','.join(problems[:-1]) + ',' + problems[-1])  # 쉼표로 연결된 문자열로 출력
    pass


def score_result(user, user_answer) :
    score_num_list=[] # 점수에 대한 리스트
    print("응시자별 채점 결과 :")
    sum_score=0 # 점수 합산을 위해 0으로 설정
    for i in range(len(user)) : # 참여자의 수만큼
        user_answer_list=[]
        correct_num_list=[]
        score_list=[]
        score=0

        for j in range(len(user_answer)): # user_answer의 길이만큼
            if  user[i]['_id'] == user_answer[j]['user_id']: # user의 id와 user_answer의 user_id와 같을시
                user_answer_list.append(user_answer[j]['user_answer'])
        for j in range(len(problem)): # problem_list 길이만큼    
                correct_num_list.append(problem[j]['correct_answer'])
                score_list.append(problem[j]['score'])
        for j in range(len(user_answer_list)): #user_anwer_list의 길이만큼       
            if user_answer_list[j] == correct_num_list[j]: # 참여자의 입력답과 정답이 같을 시
                score += score_list[j]  # 점수 배점
                coll_user_answer.update_one({"user_id":user[i]['_id'] , "problem_id" : problem[j]['_id']}, {"$set":{"user_score":problem[j]['score']}}) 
            else :
                coll_user_answer.update_one({"user_id":user[i]['_id'] , "problem_id" : problem[j]['_id']}, {"$set":{"user_score":0}})
            pass    
        
        score_num_list.append(score) # 각 점수를 score_num_list에 넣기
        print("{} : {}점".format(user[i]["user_name"], score)) #user에 있는 user_name을 출력
    
    for i in range(len(score_num_list)):  # 각 점수를 합산
        sum_score += score_num_list[i] 
        pass

    print("과목 평균 점수: {}점".format(sum_score/len(user))) # 전체 합산 점수/사용자의 수만큼 해서 전체 평균 구하기









   
