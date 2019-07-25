# Generated by Django 2.2 on 2019-07-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_mysqlinitinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_id', models.IntegerField()),
                ('username', models.CharField(default='', max_length=32)),
                ('option', models.CharField(default='', max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='', max_length=16)),
            ],
        ),
    ]
