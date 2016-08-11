from __future__ import print_function
from django.shortcuts import render

from myapp.forms import ExamForm
from myapp.models import Exam

score = 0


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def queryDb(qn_id):
    global score
    try:
        exam = Exam.objects.get(id=int(qn_id) + 1)
    except Exception:
        print(str(Exception))
        score = 0
        exam = Exam.objects.get(id=5)
    finally:
        return exam


def result(request, qn_id=None):
    # gets access to global variable
    global score
    exam = queryDb(qn_id)
    # qn_id is a unicode, convert it to int
    print(int(qn_id) + 1)

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            # returns the actual data from the form
            data = form.cleaned_data
            # returns the structure of the form
            # print(form['answer'])
            check_result(data, qn_id)
        print("SCORE " + str(score))
        return render(request, 'result.html', {
            'exam': exam,
            'score': score,
            'form': form
        })
    else:
        form = ExamForm()
        return render(request, 'result.html', {
            'exam': exam,
            'score': score,
            'form': form
        })


def check_result(data, qn_id):
    global score
    exam2 = Exam.objects.get(id=qn_id)
    if data['answer'] == exam2.answer:
        score += 1
