# Generated by Django 4.2 on 2023-04-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_student_classes_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name': 'الفصل', 'verbose_name_plural': 'الفصول'},
        ),
    ]
