# Generated by Django 4.1 on 2022-09-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(db_column='_id', primary_key=True, serialize=False),
        ),
    ]
