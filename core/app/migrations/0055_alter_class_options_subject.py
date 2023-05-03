# Generated by Django 4.1.7 on 2023-04-30 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_alter_class_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['name'], 'verbose_name': 'الحصة', 'verbose_name_plural': 'الحصص'},
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('قران', 'قران'), ('تربية اسلامية', 'تربية اسلامية'), ('لغتي', 'لغتي'), ('رياضيات', 'رياضيات'), ('علوم', 'علوم'), ('تربية بدنية', 'تربية بدنية'), ('تربية فنية', 'تربية فنية'), ('لغة انجليزية', 'لغة انجليزية'), ('اجتماعيات', 'اجتماعيات'), ('مهارات حيايتة وأسرية', 'مهارات حيايتة وأسرية'), ('التربية الرقمية', 'التربية الرقمية')], max_length=150)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
            options={
                'verbose_name': 'المادة',
                'verbose_name_plural': 'المواد',
                'ordering': ['name'],
            },
        ),
    ]
