# Generated by Django 3.2.17 on 2023-04-21 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_quizzes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.quizzes')),
            ],
            options={
                'verbose_name': 'السؤال',
                'verbose_name_plural': 'الاسئلة',
                'ordering': ['id'],
            },
        ),
    ]
