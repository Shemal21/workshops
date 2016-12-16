__author__ = 'jc350024'

scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
if scores != []:
    print("Your highest score is", max(scores))

