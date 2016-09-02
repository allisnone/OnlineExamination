from __future__ import print_function
from django.shortcuts import render

from myapp.forms import ExamForm
from myapp.models import Exam, TimeTable, Result, Subject, Student
from datetime import date

score = 0


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def is_last_question(id):
    if id == 10:
        print('RENDERING')
        return True
    return False


def start(request, qn_id=None):
    global score

    print("ID " + qn_id)
    if is_last_question(int(qn_id)):
        comment = generate_comment()
        save_result(comment)
        return render(request, 'end.html', {
            'score': score,
            'comment': comment
        })

    # gets access to global variable
    exam = query_db(qn_id)

    # qn_id is a unicode, convert it to int
    print(int(qn_id) + 1)
    form = check_form_validity(request, qn_id)
    return render(request, 'start.html', {
        'exam': exam,
        'score': score,
        'form': form
    })


def save_result(comment):
    global score
    student_result = Result(sub_id=Subject.objects.get(id=2), student_id=Student.objects.get(id=2),
                            mark=score, comment=comment, date=date.today())
    student_result.save()


def generate_comment():
    global score
    comments = ['Nice', 'Try harder next-time', 'Very good', 'Good', 'Excellent']
    if score >= 4:
        return comments[4]
    elif score >= 3:
        return comments[2]
    elif score >= 2:
        return comments[3]
    elif score >= 1:
        return comments[0]
    else:
        return comments[1]


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
    table = Result.objects.all()
    return render(request, 'result.html', {
        'table': table
    })
