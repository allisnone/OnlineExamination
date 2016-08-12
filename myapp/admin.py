from django.contrib import admin

from myapp.models import Exam, Room, Subject, TimeTable, Result, Lecturer, Student, Qualification, ClassRoom


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


class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ('id', 'sub_id', 'mark', 'date')

    def sub_id(self, instance):
        return instance.subject.subject_name


class LecturerAdmin(admin.ModelAdmin):
    model = Lecturer
    list_display = ('id', 'name', 'age', 'qualification', 'salary')


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('id', 'name', 'age', 'classroom_id', 'result_id')

    def classroom_id(self, instance):
        return instance.classroom.name

    def result_id(self, instance):
        return instance.result.mark


class QualificationAdmin(admin.ModelAdmin):
    model = Qualification


class ClassRoomAdmin(admin.ModelAdmin):
    model = ClassRoom


admin.site.register(Exam, ExamAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Student, StudentAdmin)
