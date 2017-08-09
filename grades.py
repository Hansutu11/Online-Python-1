import random
def gradeScale():
    for i in range(10):
        score = random.randint(60,100)

        if score <= 100:
            print "Score", score, "; Your Grade is a A"
        if score <= 90:
            print "Score", score, "; Your Grade is a B"
        if score <= 80:
            print "Score", score, "; Your Grade is a C"
        if score <= 70:
            print "Score", score, "; Your Grade is a D"

gradeScale()
