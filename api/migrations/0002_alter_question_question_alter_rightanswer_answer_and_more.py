# Generated by Django 4.2.4 on 2023-09-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='rightanswer',
            name='answer',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='typeofquestion',
            name='name',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='wronganswer',
            name='answer',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='wronganswer',
            name='name',
            field=models.CharField(max_length=127),
        ),
    ]