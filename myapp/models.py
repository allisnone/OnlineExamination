from __future__ import unicode_literals

from django.db import models


class Exam(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=50)
