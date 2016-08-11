from django import forms

from myapp.models import Exam


class ExamForm(forms.Form):
    CHOICES = [('TRUE', 'true'), ('FALSE', 'false')]
    answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

