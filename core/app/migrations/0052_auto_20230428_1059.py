# Generated by Django 3.2.17 on 2023-04-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'بيانات المدرسة - School Data',
                'verbose_name_plural': 'بيانات المدرسة - School Data',
            },
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_of_birth',
            new_name='birthdate',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='major',
            field=models.CharField(choices=[('قران', 'قران'), ('تربية اسلامية', 'تربية اسلامية'), ('لغتي', 'لغتي'), ('رياضيات', 'رياضيات'), ('علوم', 'علوم'), ('تربية بدنية', 'تربية بدنية'), ('تربية فنية', 'تربية فنية'), ('لغة انجليزية', 'لغة انجليزية'), ('اجتماعيات', 'اجتماعيات'), ('مهارات حيايتة وأسرية', 'مهارات حيايتة وأسرية'), ('التربية الرقمية', 'التربية الرقمية')], max_length=150, null=True, verbose_name='التخصص'),
        ),
    ]