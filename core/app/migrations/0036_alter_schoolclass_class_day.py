# Generated by Django 3.2.17 on 2023-04-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_schoolclass_class_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclass',
            name='class_day',
            field=models.CharField(choices=[(0, 'الأحد'), (1, 'الأثنين'), (2, 'الثلاثاء'), (3, 'الأربعاء'), (4, 'الخميس')], max_length=50, null=True),
        ),
    ]
