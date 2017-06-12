import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model): # inherits from superclass models.Model
    question_text = models.CharField(max_length=200) # charfield (string) requires maxlength
    pub_date = models.DateTimeField('date published') #datetime field

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text