from django import forms


class ExamForm(forms.Form):
    CHOICES = [('TRUE', 'true'), ('FALSE', 'false')]
    answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

