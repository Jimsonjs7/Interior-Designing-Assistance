# Generated by Django 5.1.4 on 2024-12-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
            ],
        ),
    ]