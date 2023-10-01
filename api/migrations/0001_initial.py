# Generated by Django 4.2.5 on 2023-10-01 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='RightAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='WrongAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=127)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='right_answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.rightanswer'),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('image', models.ImageField(upload_to='')),
                ('questions', models.ManyToManyField(to='api.question')),
            ],
        ),
    ]
