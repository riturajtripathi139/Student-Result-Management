# Generated by Django 2.2.2 on 2019-07-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuser', models.CharField(max_length=100)),
                ('fpass', models.CharField(max_length=100)),
            ],
        ),
    ]
