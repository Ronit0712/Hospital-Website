# Generated by Django 5.0.1 on 2024-02-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_homecardmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
            ],
        ),
    ]