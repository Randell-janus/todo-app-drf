# Generated by Django 4.1 on 2022-09-16 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
