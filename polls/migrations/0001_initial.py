# Generated by Django 3.0.5 on 2020-04-22 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('m', '男'), ('w', '女')], default='m', max_length=1, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='SassUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='公司名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='', max_length=50, verbose_name='内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Interviewer', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='进程名称')),
                ('status', models.CharField(choices=[('p', '通过'), ('f', '未通过'), ('d', '进行中')], default='d', max_length=1, verbose_name='面试状态')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Interviewer', verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='interviewer',
            name='sass_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SassUser', verbose_name='Sass用户'),
        ),
    ]
