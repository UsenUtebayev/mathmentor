# Generated by Django 4.2.4 on 2023-09-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_question_wrong_answers_question_wrong_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='questions',
        ),
        migrations.AddField(
            model_name='level',
            name='questions',
            field=models.ManyToManyField(to='api.question'),
        ),
    ]