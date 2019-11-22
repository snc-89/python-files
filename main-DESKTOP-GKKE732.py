from assessmentv3 import *

portfolio = Assessment(20,20,20)
attendance = Assessment(10,10,10)
project = Assessment(30,30,30)
final = Assessment(0,100,40)
print("\ncomp257")
Unit(final, [portfolio, attendance, project]).marksNeededInExam()

weekly_problems = Assessment(10,10,10)
attendance = Assessment(10,10,10)
assignment_1 = Assessment(13.5,15,15)
assignment_2 = Assessment(8,15,15)
final.weight = 50
print("\ncomp255")
Unit(final, [weekly_problems, attendance,assignment_1,assignment_2]).marksNeededInExam() 

inClass = Assessment(6,6,16)
java_practice = Assessment(73.75,100,(44/3))
design_patterns = Assessment(93.25,100,(44/3))
concurrency = Assessment(50.25,100,(44/3))
ass1 = Assessment(8,8,8)
ass2 = Assessment(14,14,14)
ass3 = Assessment(18,18,18)
final.weight = 44
assessment_list = [inClass,java_practice,design_patterns,
                    concurrency,ass1,ass2,ass3]
comp229 = Unit(final,assessment_list)
print("\ncomp229 total: ",comp229.unitTotal())
comp229.marksNeededInExam()

final.weight = 50
ass1 = Assessment(19.1,20,20)
ass2 = Assessment(20,20,20)
quiz1 = Assessment(30,30,5)
quiz2 = Assessment(25,30,5)
print("\ncomp202")
Unit(final,[ass1,ass2,quiz1,quiz2]).marksNeededInExam()