# 문제 제출지 작성하기

class issuesubmit :
    def __init__(self):
        self.problem_list = [] # 문제 리스트가 들어갈 곳
        self.proble_manswer = [] # 문제 id와 연동해서 문제 답이 들어갈 곳

    def mongoconnect(self): # 몽고디비와 연결하는 함수
        from pymongo import MongoClient
        Mongoclient = MongoClient("mongodb://localhost:27017")
        database = Mongoclient("toy_nosqls")
        self.problem_list = database("problem_list")
        self.problem_answer = database("problem_answer")
        
    def makeproblem(self): # 문제와 답을 넣는 것
        

        
        

