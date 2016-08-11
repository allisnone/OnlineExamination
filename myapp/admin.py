from django.contrib import admin

from myapp.models import Exam


class ExamAdmin(admin.ModelAdmin):
    model = Exam
    list_display = ('id', 'question', 'answer')

admin.site.register(Exam, ExamAdmin)
