from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.0.145:27017")    # mongodb 접속
database = mongoClient["toy_nosqls"]   # database 연결
# database[collection_name]        # collection 작업

coll_problem_list = database['problem_list']
coll_problem_answer = database['problem_answer']
coll_user = database['user']
coll_user_answer = database['user_answer']

problem = list(coll_problem_list.find({}))
problem_answer = list(coll_problem_answer.find({}))
user = list(coll_user.find({}))
user_answer = list(coll_user_answer.find({}))

# -----------------------------------------------------

# 각 문항 정답 출력에 대한 구문
def answer_data():
    print("-------------------")
    print("각 문항 정답 : ", end="")
    for i in range(len(problem)):
        # if i < 2 :
        print("{}".format(problem[i]['correct_answer']), end=",")
        # else :
        # print("{}".format(problem[i]['correct_answer']))
        pass
    print("")

def score_result() :
    score_num_list=[]
    print("응시자별 채점 결과 :")
    sum_score=0
    for i in range(len(user)) :
        user_answer_list=[]
        correct_num_list=[]
        score_list=[]
        score=0

        for j in range(len(user_answer)):
            if  user[i]['_id'] == user_answer[j]['user_id']:
                user_answer_list.append(user_answer[j]['user_answer'])
                # print(user_answer_list)
        for j in range(len(problem)):        
                correct_num_list.append(problem[j]['correct_answer'])
                score_list.append(problem[j]['score'])
                # print(correct_num_list)
        for j in range(len(user_answer_list)):        
            if user_answer_list[j] == correct_num_list[j]:
                score += score_list[j]
                coll_user_answer.update_one({"user_id":user[j]['_id'] , "problem_id" : problem[j]}, {"$set":{"user_score":problem[j]['score']}})
            else :
                coll_user_answer.update_one({"user_id":user[j]['_id'] , "problem_id" : problem[j]}, {"$set":{"user_score":0}})      
            pass    

        score_num_list.append(score)
        print("{} : {}점".format(user[i]["user_name"], score)) #user에 있는 user_name을 출력

    for i in range(len(score_num_list)):
        sum_score += score_num_list[i]
        pass

    print("과목 평균 점수: {}점".format(sum_score/len(user)))









   
