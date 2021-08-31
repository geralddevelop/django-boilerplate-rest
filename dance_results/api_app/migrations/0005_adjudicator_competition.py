# Generated by Django 3.2.6 on 2021-08-13 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_rename_ajudicator_adjudicator'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjudicator',
            name='competition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_app.competition'),
            preserve_default=False,
        ),
    ]
