# Generated by Django 3.2.17 on 2023-04-22 17:29

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_course_my_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='my_column',
        ),
        migrations.AddField(
            model_name='course',
            name='my_column',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('عصف ذهني', 'عصف ذهني'), ('خرائط ذهنية', 'خرائط ذهنية'), ('الصف المقلوب', 'الصف المقلوب'), ('التعلم التعاوني', 'التعلم التعاوني'), ('التعلم الذاتي', 'التعلم الذاتي'), ('التجارب', 'التجارب')], max_length=71, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='العمر'),
        ),
    ]