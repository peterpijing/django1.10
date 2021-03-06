from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Questions(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

class Choice(models.Model):
    question = models.ForeignKey(Questions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


