# Generated by Django 2.2.1 on 2019-07-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='award_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='awards',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
