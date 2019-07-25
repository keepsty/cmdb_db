# Generated by Django 2.2 on 2019-07-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_delete_mysqlinitinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlInitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.GenericIPAddressField()),
                ('user', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('version', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('change_time', models.DateTimeField(auto_now=True)),
                ('app_name', models.CharField(default='mysql', max_length=20)),
            ],
            options={
                'db_table': 'MysqlInitInfo',
                'unique_together': {('app_name', 'server_ip')},
            },
        ),
    ]