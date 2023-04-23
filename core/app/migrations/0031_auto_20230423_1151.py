# Generated by Django 3.2.17 on 2023-04-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20230422_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STUDENT', 'Student'), ('TEACHER', 'Teacher')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='major',
            field=models.CharField(choices=[('قران', 'قران'), ('تربية اسلامية', 'تربية اسلامية'), ('لغتي', 'لغتي'), ('رياضيات', 'رياضيات'), ('علوم', 'علوم'), ('تربية بدنية', 'تربية بدنية'), ('تربية فنية', 'تربية فنية'), ('لغة انجليزية', 'لغة انجليزية'), ('اجتماعيات', 'اجتماعيات'), ('مهارات حيايتة وأسرية', 'مهارات حيايتة وأسرية'), ('التربية الرقمية', 'التربية الرقمية')], max_length=100, null=True, verbose_name='التخصص'),
        ),
    ]