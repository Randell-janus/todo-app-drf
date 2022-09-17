# Generated by Django 4.1 on 2022-09-16 04:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_todo_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
