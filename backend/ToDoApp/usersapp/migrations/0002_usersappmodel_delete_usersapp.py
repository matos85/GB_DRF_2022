# Generated by Django 4.0.4 on 2022-05-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersappModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
        migrations.DeleteModel(
            name='Usersapp',
        ),
    ]