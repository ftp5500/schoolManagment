# Generated by Django 4.1.7 on 2023-05-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_rename_classroom_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='section',
            field=models.CharField(choices=[('1', 'أ'), ('2', 'ب'), ('3', 'ج'), ('4', 'د')], max_length=150, null=True, verbose_name='الشعبة'),
        ),
    ]