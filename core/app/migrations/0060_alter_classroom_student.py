# Generated by Django 4.1.7 on 2023-05-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_remove_classroom_student_classroom_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(to='app.student'),
        ),
    ]