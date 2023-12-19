## 이곳에 클래스 넣기

#문제 제출지 작성에 필요한 클래스 호출

from problem_withmongo_sky import Issuesubmit
import problem_withmongo_youngji

issuesubmit = Issuesubmit()
issuesubmit.mongoconnect()
issuesubmit.makeproblem2()

problem_withmongo_youngji.solving_problem()
problem_withmongo_youngji.end()

