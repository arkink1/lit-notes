# Generated by Django 3.0.6 on 2020-12-20 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201220_2043'),
        ('plays', '0003_auto_20201220_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='play',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Play'),
        ),
    ]
