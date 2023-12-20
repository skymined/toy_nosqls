## 이곳에 클래스 넣기

#문제 제출지 작성에 필요한 클래스 호출

from problem_withmongo_sky import Issuesubmit
import problem_withmongo_youngji
import score_sum_kgh

# issuesubmit = Issuesubmit()
# issuesubmit.makeproblem()

# problem_withmongo_youngji.solving_problem()
# problem_withmongo_youngji.end()

pro = score_sum_kgh.problem
user = score_sum_kgh.user
user_an = score_sum_kgh.user_answer
score_sum_kgh.answer_data(pro)
score_sum_kgh.score_result(user, user_an)




