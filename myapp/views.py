from django.shortcuts import render


def index(request):
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who']
    return render(request, 'index.html', {
        'qn': qn[1]
    })


def result(request, qn_id):
    counter = 0
    if counter >= 2:
        counter = 0
    else:
        counter += 1
    qn = ['what is your name?', 'when did NASA step on the moon?', 'who stepped on the moon?']
    if request.method == 'POST':
        return render(request, 'result.html', {
            'qn_id': qn[counter]
        })

    return render(request, 'result.html', {
        'qn_id': 'error'
    })
