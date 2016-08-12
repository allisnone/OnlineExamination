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


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('id', 'name', 'age', 'classroom_id')

    def classroom_id(self, instance):
        return instance.classroom.name


class ResultAdmin(admin.ModelAdmin):
    model = Result
    # names listed must not be names in table
    list_display = ('id', 'sub_id', 'student_id', 'mark', 'date', 'comment')

    # these methods are not really necessary
    # name above must match the method
    # def sub_id(self, instance):
    #     return instance.subject.subject_name
    #
    # def student_id(self, instance):
    #     # get student_id then traverse to get the name
    #     return instance.student.name


class LecturerAdmin(admin.ModelAdmin):
    model = Lecturer
    list_display = ('id', 'name', 'age', 'qualification', 'salary')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Qualification)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(ClassRoom)
