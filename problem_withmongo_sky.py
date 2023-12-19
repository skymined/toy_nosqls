# 문제 제출지 작성하기

class Issuesubmit :
    def __init__(self):
        self.problem_list = [] # 문제 리스트가 들어갈 곳
        self.problem_answer = [] # 문제 id와 연동해서 문제 답이 들어갈 곳

    def mongoconnect(self): # 몽고디비와 연결하는 함수
        from pymongo import MongoClient
        Mongoclient = MongoClient("mongodb://192.168.0.145:27017")
        database = Mongoclient["toy_nosqls"]
        self.problem_list = database["problem_list"]
        self.problem_answer = database["problem_answer"]
        
    def makeproblem(self): # 문제와 답을 넣는 것
        problem_type = int(input("문제 유형을 입력하세요.(n지선다형) : "))
        problem_count = int(input("문항 수를 입력하세요.(n문항) : "))
        for i in range(problem_count):
            print("문제와 선택지를 입력하세요.")
            problem_1 = input("문항{} ".format(i+1))
            result = self.problem_list.insert_one({"Question" : problem_1})
            problem_id = result.inserted_id
            for j in range(problem_type):
                problem_1_answer = input("{}. ".format(j+1))
                self.problem_answer.insert_one({"Question_id":problem_id, "Answer_num" : j+1, "Answer" : problem_1_answer})
            score = int(input("점수 : "))
            correct_answer = int(input("정답 : "))
            self.problem_list.update_many({"Question" : problem_1}, {"$set":{"score":score, "correct_answer":correct_answer}})

                


        
        

