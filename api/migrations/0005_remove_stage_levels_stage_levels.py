# Generated by Django 4.2.4 on 2023-09-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_level_questions_level_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='levels',
        ),
        migrations.AddField(
            model_name='stage',
            name='levels',
            field=models.ManyToManyField(to='api.level'),
        ),
    ]
