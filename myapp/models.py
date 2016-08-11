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
