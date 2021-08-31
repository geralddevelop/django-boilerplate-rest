# Generated by Django 3.2.6 on 2021-08-14 04:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0013_auto_20210814_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='competition',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 4, 9, 18, 458338)),
        ),
        migrations.AddField(
            model_name='competition',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 4, 9, 18, 458309)),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api_app.competition')),
                ('dances', models.ManyToManyField(to='api_app.Dance')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
