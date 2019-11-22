from random import randrange
with open('comp257_questions.txt', 'r') as f:
    questions = f.read()
with open('comp257_answers.txt','r') as f:
    answers = f.read()
questions = questions.split('\n')
answers = answers.split('...')

answer_arr = []
for i in range(len(questions)):
    idx = randrange(len(questions))
    print(i)
    print(questions.pop(idx))
    answer_arr.append(answers.pop(idx))

for i,answer in enumerate(answer_arr):
    print(i)
    print(answer)