from __future__ import unicode_literals

from django.db import models


class Exam(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=50)

    def __unicode__(self):
        return self.question


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.subject_name


class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.room_name


class TimeTable(models.Model):
    sub_id = models.ForeignKey(Subject)
    room_id = models.ForeignKey(Room)
    time = models.TimeField()
    date = models.DateField()


class Qualification(models.Model):
    level = models.CharField(max_length=255)

    def __unicode__(self):
        return self.level


class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    qualification = models.ForeignKey(Qualification)
    salary = models.IntegerField()

    def __unicode__(self):
        return self.name


class ClassRoom(models.Model):
    lecturer_id = models.ForeignKey(Lecturer)
    room_id = models.ForeignKey(Room)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    classroom_id = models.ForeignKey(ClassRoom)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name


class Result(models.Model):
    sub_id = models.ForeignKey(Subject)
    student_id = models.ForeignKey(Student)
    mark = models.FloatField()
    date = models.DateField()
    comment = models.CharField(max_length=255)

    def __unicode__(self):
        # the database requires string to identify 'Result object'
        return str(self.comment)
