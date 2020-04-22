from django.db import models
from django.contrib.auth.models import User


class SassUser(models.Model):
    name = models.CharField('公司名', max_length=20)
    password = models.CharField('密码', max_length=20)


class Interviewer(models.Model):
    name = models.CharField('姓名', max_length=20)
    age = models.IntegerField('年龄', default=0)
    CHOICES = (
        ('m', '男'),
        ('w', '女'),
    )
    sex = models.CharField(
        '性别',
        max_length=1,
        choices=CHOICES,
        default='m')
    sass_user = models.ForeignKey(
        SassUser,
        verbose_name='Sass用户',
        null=False,
        on_delete=models.CASCADE)


class Message(models.Model):
    info = models.CharField('内容', max_length=50, default='')
    author = models.ForeignKey(
        Interviewer,
        verbose_name='用户',
        null=False,
        on_delete=models.CASCADE)


class InterviewProcess(models.Model):
    name = models.CharField('进程名称', max_length=20, default='')
    interviewer = models.ForeignKey(
        Interviewer,
        verbose_name='用户',
        null=False,
        on_delete=models.CASCADE)
    CHOICES = (
        ('p', '通过'),
        ('f', '未通过'),
        ('d', '进行中'),
    )
    status = models.CharField(
        '面试状态',
        max_length=1,
        choices=CHOICES,
        default='d')
