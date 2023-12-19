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

for i in range(len())




# problem = coll_problem.find()


# for i in range(user_id_list):

#     for j in range(problem_id_list):



#         user_answer = []

#         if user_answer[1] == answer[1] : 
#             coll_user_answer.update_one( { }, "$set":"user_score":score[1])
   
