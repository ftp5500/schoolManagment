# Generated by Django 3.2.17 on 2023-04-27 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_remove_subject_class_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='course',
            name='which_class',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizzes',
            name='course',
        ),
        migrations.RemoveField(
            model_name='schoolclass',
            name='class_group',
        ),
        migrations.RemoveField(
            model_name='schoolclass',
            name='class_subject',
        ),
        migrations.RemoveField(
            model_name='schoolclass',
            name='class_time',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='class_time',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='ClassTime',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quizzes',
        ),
        migrations.DeleteModel(
            name='SchoolClass',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
