# Generated by Django 4.0.4 on 2023-02-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=64, verbose_name='Projectname')),
                ('repo_link', models.URLField(verbose_name='Repolink')),
                ('authors', models.CharField(max_length=128, verbose_name='Authors')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField(verbose_name='Creationdate')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updatedate')),
                ('user', models.CharField(max_length=64, verbose_name='User')),
                ('status', models.CharField(choices=[('active', 'активно'), ('close', 'закрыто')], max_length=300)),
                ('projeck', models.ManyToManyField(to='todo.project')),
            ],
        ),
    ]
