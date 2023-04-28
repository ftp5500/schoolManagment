# Generated by Django 3.2.17 on 2023-04-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_auto_20230425_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('1', 'الحصة الأولى'), ('2', 'الحصة الثانية'), ('3', 'الحصة الثالثة'), ('4', 'الحصة الرابعة'), ('5', 'الحصة الخامسة'), ('6', 'الحصة السادسة'), ('7', 'الحصة السابعة'), ('8', 'الحصة الثامنة'), ('9', 'الحصة التاسعة')], max_length=150, verbose_name='الحصة')),
                ('starting', models.TimeField(null=True, verbose_name='بداية الحصة')),
                ('ending', models.TimeField(null=True, verbose_name='نهاية الحصة')),
            ],
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ['day'], 'verbose_name': 'الحصة', 'verbose_name_plural': 'الحصص'},
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='ending',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='starting',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='title',
        ),
        migrations.AddField(
            model_name='timetable',
            name='class_time',
            field=models.ManyToManyField(to='app.ClassTime'),
        ),
    ]