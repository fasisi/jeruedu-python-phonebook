from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Phone(models.Model):
    name = models.CharField(null = False, max_length=200)
    address = models.CharField(null = True, max_length=1000)
    hobby = models.TextField(null = True)
    phone = models.CharField(null = True, max_length=150)
    dob = models.DateField(null = True)
    is_delete = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now = True)
    delete_time = models.DateTimeField(null = True)

class User(models.Model):
    name = models.CharField(null = False, max_length=100)
    username = models.CharField(null = False, max_length=100)
    password = models.CharField(null = False, max_length = 200)