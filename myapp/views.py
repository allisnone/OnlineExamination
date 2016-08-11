from __future__ import print_function
from django.shortcuts import render

from myapp.models import Exam


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def result(request, qn_id=None):
    try:
        exam = Exam.objects.get(id=int(qn_id) + 1)
    except Exception:
        print(str(Exception)+'BUG')
        exam = Exam.objects.get(id=5)
    # qn_id is a unicode, convert it to int
    print(int(qn_id) + 1)

    if request.method == 'POST':
        return render(request, 'result.html', {
            'exam': exam,
        })

    return render(request, 'result.html', {
        'exam': exam
    })
