from django.db import models

# Create your models here.
#this is where we add the database models
#there would be a primary key id made by default
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_data = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #when a question is deleted, then the choices are also deleted
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return choice_text