# Generated by Django 4.2.7 on 2023-12-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadosma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='address',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='url2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
