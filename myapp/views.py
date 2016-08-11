from __future__ import print_function
from django.shortcuts import render

from myapp.forms import ExamForm
from myapp.models import Exam, TimeTable

score = 0


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def start(request, qn_id=None):
    # gets access to global variable
    global score
    exam = query_db(qn_id)
    # qn_id is a unicode, convert it to int
    print(int(qn_id) + 1)
    form = check_form_validity(request, qn_id)
    return render(request, 'start.html', {
        'exam': exam,
        'score': score,
        'form': form
    })


def check_form_validity(request, qn_id):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            # returns the actual data from the form
            data = form.cleaned_data
            # returns the structure of the form
            # print(form['answer'])
            check_result(data, qn_id)
        print("SCORE " + str(score))
    else:
        form = ExamForm()
    return form


def query_db(qn_id):
    global score
    try:
        exam = Exam.objects.get(id=int(qn_id) + 1)
    except Exception:
        print(str(Exception))
        score = 0
        exam = Exam.objects.get(id=5)
    finally:
        return exam


def check_result(data, qn_id):
    global score
    exam2 = Exam.objects.get(id=qn_id)
    if data['answer'] == exam2.answer:
        score += 1


def time_table(request):
    table = TimeTable.objects.all()
    return render(request, 'timeTable.html', {
        'table': table
    })


def result(request):
    # TODO make registration and result
    table = TimeTable.objects.all()
    return render(request, 'result.html', {
        'table': table
    })