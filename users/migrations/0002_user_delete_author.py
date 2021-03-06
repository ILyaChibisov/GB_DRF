# Generated by Django 4.0.4 on 2022-05-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='Username')),
                ('first_name', models.CharField(max_length=64, verbose_name='First_name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last_name')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
