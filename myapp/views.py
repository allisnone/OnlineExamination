from django.shortcuts import render


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[2]
    })


def result(request, qn_id):
    if request.method == 'POST':
        return render(request, 'result.html', {
            'qn_id': request.POST['first']
        })

    return render(request, 'result.html', {
        'qn_id': 'error'
    })
