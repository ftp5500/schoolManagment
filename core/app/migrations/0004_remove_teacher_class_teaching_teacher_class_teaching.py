# Generated by Django 4.2 on 2023-04-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_class_name_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='class_teaching',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_teaching',
            field=models.ManyToManyField(default='', to='app.class_name'),
        ),
    ]