from __future__ import print_function
from django.shortcuts import render

from myapp.models import Exam

score = 0


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def result(request, qn_id=None):
    # gets access to global variable
    global score

    try:
        exam = Exam.objects.get(id=int(qn_id) + 1)
    except Exception:
        print(str(Exception) + 'BUG')
        score = 0
        exam = Exam.objects.get(id=5)

    # qn_id is a unicode, convert it to int
    print(int(qn_id) + 1)

    if request.method == 'POST':
        if request.POST['answer'] == exam.answer:
            score += 1

        print("SCORE " + str(score))
        return render(request, 'result.html', {
            'exam': exam,
            'score': score
        })

    return render(request, 'result.html', {
        'exam': exam,
        'score': score
    })
