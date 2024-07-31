# Generated by Django 5.0.1 on 2024-02-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0010_blogmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=100)),
                ('cinput', models.CharField(max_length=100)),
                ('cdays', models.CharField(max_length=100)),
                ('ctime', models.TimeField(max_length=100)),
                ('cno1', models.CharField(max_length=15)),
                ('cno2', models.CharField(max_length=15)),
            ],
        ),
    ]
