# Generated by Django 4.2 on 2023-04-17 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_class_name_alter_subject_name_student_student_class_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class_name',
            options={'verbose_name': 'Class Name', 'verbose_name_plural': 'Classes'},
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='class_teaching',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_teaching',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app.class_name'),
        ),
    ]