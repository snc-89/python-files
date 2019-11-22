from assessmentv3 import *

inClass = Assessment(6,6,16)
module_1 = Assessment(84.5,100,(44/3))
module_2 = Assessment(87.0,100,(44/3))
module_3 = Assessment(81,100,(44/3))
ass1 = Assessment(8,8,8)
ass2 = Assessment(67,100,14)
ass3 = Assessment(14,18,18)
final = Assessment(0,1,44)
assessment_list = [inClass,module_1,module_2,module_3,ass1,ass2,ass3]
comp229 = Unit(final,assessment_list)
print("comp229: ",comp229.unitTotal())
comp229.marksNeededInExam()

attendance = Assessment(10,10,10)
homework = Assessment(10,10,10)
assignment_1 = Assessment(13.5,15,15)
assignment_2 = Assessment(10,15,15)
exam = Assessment(35,50,50)
assessments = [attendance,homework,assignment_1,assignment_2]
comp255 = Unit(exam,assessments)
print("comp255", comp255.unitTotal())
comp255.marksNeededInExam()

attendance = Assessment(10,10,10)
portfolio = Assessment(20,20,20)
project = Assessment(25.5,30,30)
exam = Assessment(0,40,40)
assessments = [attendance,portfolio,project]
comp257 = Unit(exam,assessments)
print("comp257 ", comp257.unitTotal())
comp257.marksNeededInExam()

quiz_1 = Assessment(5,5,5)
quiz_2 = Assessment(25,30,5)
c_lab = Assessment(19.1,20,20)
bomb_lab = Assessment(20,20,20)
exam = Assessment(85,100,50)
assessments = [quiz_1,quiz_2,c_lab,bomb_lab]
comp202 = Unit(exam, assessments)
print("comp202",comp202.unitTotal())
comp202.marksNeededInExam()