import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

        # __str__pythonが元から定義している特殊な関数だということを示しているわけです。
        # classのオブジェクトを文字列で表現するstrという特殊メソッドに、classのオブジェクト自身を表現するselfを引数として渡したもの
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text