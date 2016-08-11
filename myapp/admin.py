from django.contrib import admin

from myapp.models import Exam, Room, Subject, TimeTable


class ExamAdmin(admin.ModelAdmin):
    model = Exam
    list_display = ('id', 'question', 'answer')


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ('id', 'room_name')


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('id', 'subject_name')


class TimeTableAdmin(admin.ModelAdmin):
    model = TimeTable
    list_display = ('id', 'sub_id', 'room_id', 'time', 'date')

    def sub_id(self, instance):
        return instance.subject.subject_name

    def room_id(self, instance):
        return instance.room.room_name


admin.site.register(Exam, ExamAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
