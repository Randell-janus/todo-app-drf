# Generated by Django 4.1 on 2022-09-16 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_todo_created_todo_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
